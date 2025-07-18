from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import OrderItem, Order
from .forms import OrderCreateForm


def order_create(request):
    """Create a new order"""
    cart = Cart(request)
    if len(cart) == 0:
        messages.error(request, 'Your cart is empty.')
        return redirect('cart:cart_detail')

    # Get detailed cart items
    cart_items = cart.get_products_detail()

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.total_amount = cart.get_total_price()
            order.save()

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            # Clear the cart
            cart.clear()
            messages.success(request, f'Order {order.id} created successfully!')
            return redirect('orders:order_created', order_id=order.id)
    else:
        # Pre-fill form with user data if authenticated
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
            }
        form = OrderCreateForm(initial=initial_data)

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': cart.get_total_price(),
        'total_quantity': len(cart),
        'form': form,
    }

    return render(request, 'orders/order/create.html', context)

def order_created(request, order_id):
    """Order confirmation page"""
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/order/created.html', {'order': order})


@login_required
def order_history(request):
    """Display user's order history"""
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'orders/order/history.html', {'orders': orders})
