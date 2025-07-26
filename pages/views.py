from django.shortcuts import render
from products.models import Product, Category


def home(request):
    """Homepage with featured products and categories"""
    featured_products = Product.objects.filter(featured=True, is_active=True)[:8]
    categories = Category.objects.all()[6:]
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
    }
    return render(request, 'pages/home.html', context)


def about(request):
    """About page"""
    return render(request, 'pages/about.html')


def contact(request):
    """Contact page"""
    return render(request, 'pages/contact.html')


def faq(request):
    """FAQ page"""
    return render(request, 'pages/faq.html')


def legal(request):
    """Legal notice page"""
    return render(request, 'pages/legal.html')


def privacy(request):
    """Privacy policy page"""
    return render(request, 'pages/privacy.html')

def services(request):
    """Term services policy page"""
    return render(request, 'pages/services.html')

def shipping(request):
    """Shipping Policy"""
    return render(request, 'pages/shipping.html')


def returns_policy(request):
    """Returns Policy"""
    return render(request, 'pages/returns_policy.html')