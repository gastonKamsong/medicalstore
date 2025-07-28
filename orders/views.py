from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import OrderItem, Order
from .forms import OrderCreateForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_admin_order_email(order, cleaned_data):
    """Send order confirmation email to admin"""
    admin_email = settings.ADMIN_EMAIL  # Add to settings.py
    
    subject = f'🛒 New Order #{order.id} - {order.total_amount}€'
    body = render_to_string('emails/admin_order_notification.html', {
        'order': order,
        'cleaned_data': cleaned_data,
        'payment_method': cleaned_data.get('payment_method', 'N/A')
    })
    
    email = EmailMessage(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [admin_email],
        cc=[settings.SALES_EMAIL] if hasattr(settings, 'SALES_EMAIL') else None
    )
    email.content_subtype = 'html'
    email.send()

def order_create(request):
    """Create a new order and handle bank payment email if needed"""
    cart = Cart(request)
    if len(cart) == 0:
        messages.error(request, 'Your cart is empty.')
        return redirect('cart:cart_detail')

    cart =cart.get_products_detail()
    cart_items = []

    for item in cart:
        product = item['product']
        quantity = item['quantity']
        weight = item.get('weight', 10)  # Default to 10g
        
        # Calculate pricing based on weight
        discount = calculate_discount(weight)
        base_price = float(product.price)
        unit_price = base_price * (1 - discount)
        total_price = unit_price * weight * quantity
        
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'weight': weight,
            'total_weight': weight * quantity,
            'base_price': base_price,
            'unit_price': unit_price,
            'total_price': round(total_price, 2),
            'discount_percentage': int(discount * 100)
        })
    
    print(cart_items)
    # Calculate totals
    total_price = round(sum(item['total_price'] for item in cart_items), 2)
    total_weight = round(sum(item['weight'] for item in cart_items), 2)
    total_discount = round(sum(
        (item['base_price'] * item['weight'] * item['quantity']) - item['total_price'] 
        for item in cart_items
    ), 2)
    

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.total_amount = total_price
            order.save()

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['base_price'],
                    quantity=item['quantity'],
                    weight=item['weight'],
                )

            cart.clear()
            messages.success(request, f'Order {order.id} created successfully!')

            # Send bank info email if payment method is bank
            payment_method = form.cleaned_data.get('payment_method')
            customer_email = form.cleaned_data.get('email')
            print("payment_method")
            print(payment_method)
            print(form.cleaned_data)
            if payment_method == 'bank_transfer' and customer_email:
                subject = f'🌿 GreenMed Store - Instructions for Bank Transfer (Order #{order.id})'
                body = render_to_string('emails/bank_instructions.html', {
                    'order': order,
                    'customer_email': customer_email
                })
                email = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [customer_email])
                email.content_subtype = 'html'  # Set content type to HTML
                email.send()
            else:
                subject = f'🌿 GreenMed Store - Instructions for Bank Transfer (Order #{order.id})'
                body = render_to_string('emails/bank_instructions.html', {
                    'order': order,
                    'customer_email': customer_email
                })
                email = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [customer_email])
                email.content_subtype = 'html'  # Set content type to HTML
                email.send()


            # 2. Send admin email notification
            send_admin_order_email(order, form.cleaned_data)
            
            return redirect('orders:order_created', order_id=order.id)

    else:
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
        'total_price': total_price,
        'total_price_withouth_discount': total_price + total_discount,
        'total_discount': total_discount,
        'total_quantity': sum(item['quantity'] for item in cart_items),
        'form': form,
        'total_weight':total_weight
    }

    return render(request, 'orders/order/create.html', context)

def order_created(request, order_id):
    """Order confirmation page"""
    order = Order.objects.get(id=order_id)
    # for item in order.items.all:
    print(order.items.all)
    return render(request, 'orders/order/created.html', {'order': order})


@login_required
def order_history(request):
    """Display user's order history"""
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'orders/order/history.html', {'orders': orders})

def calculate_discount(weight):
    """Helper function to calculate discount based on weight"""
    if weight >= 1000:
        return 0.30
    elif weight >= 500:
        return 0.20
    elif weight >= 100:
        return 0.10
    elif weight >= 50:
        return 0.05
    return 0