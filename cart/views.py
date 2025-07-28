from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm, CartUpdateWeightForm  # Added the weight form


@require_POST
def cart_add(request, product_id):
    """Add a product to the cart with weight support"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            weight=cd.get('weight', 10),  # Default to 10g if not provided
            override_quantity=cd['override'],
            override_weight=cd.get('override_weight', False)
        )
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


@require_POST
def cart_update_weight(request, product_id):
    """Update product weight in the cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartUpdateWeightForm(request.POST)
    
    if form.is_valid():
        weight = form.cleaned_data['weight']
        cart.add(
            product=product,
            quantity=1,  # Maintain current quantity
            weight=weight,
            override_quantity=True,
            override_weight=True
        )
        messages.success(request, f'Updated weight for {product.name}.')
    return redirect('cart:cart_detail')


def cart_detail(request):
    """Display cart contents with weight selection and dynamic pricing"""
    cart = Cart(request)
    
    # print(
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
            'discount_percentage': int(discount * 100),
            'available_weights': [10, 50, 100, 500,1000],
            'update_quantity_form': CartAddProductForm(initial={
                'quantity': quantity,
                'override': True
            }),
            'update_weight_form': CartUpdateWeightForm(initial={
                'weight': weight
            })
        })
    
    print(cart_items)
    # Calculate totals
    total_price = round(sum(item['total_price'] for item in cart_items), 2)
    total_discount = round(sum(
        (item['base_price'] * item['weight'] * item['quantity']) - item['total_price'] 
        for item in cart_items
    ), 2)
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price,
        'total_price_withouth_discount': total_price + total_discount,
        'total_discount': total_discount,
        'total_quantity': sum(item['quantity'] for item in cart_items),
    }
    
    return render(request, 'cart/detail.html', context)


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