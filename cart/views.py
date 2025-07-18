from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from products.models import Product
from .models import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    """Add a product to the cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                override_quantity=cd['override'])
        messages.success(request, f'{product.name} added to cart.')
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    """Remove a product from the cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'{product.name} removed from cart.')
    return redirect('cart:cart_detail')


def cart_detail(request):
    """Display cart contents"""
    cart = Cart(request)
    details = cart.get_products_detail()
    for item in details:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })
    context = {
        'cart': cart,
        'cart_items': details,
        'total_price': cart.get_total_price(),
        'total_quantity': len(cart),
    }
    return render(request, 'cart/detail.html', context)

