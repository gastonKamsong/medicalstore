from django.shortcuts import render
from products.models import Product, Category


def home(request):
    """Homepage with featured products and categories"""
    featured_products = Product.objects.filter(featured=True, is_active=True)[:8]
    categories = Category.objects.all()
    
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

def crypto_guide(request):
    """crypto guide page"""
    return render(request, 'pages/crypto_guide.html')

from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils.translation import activate, get_language
from django.urls import translate_url

def change_language(request):
    if request.method == 'POST':
        lang_code = request.POST.get('language')
        next_url = request.POST.get('next')
        
        if lang_code in dict(settings.LANGUAGES).keys():
            # Activate the language for this user session
            activate(lang_code)
            request.session[settings.LANGUAGE_SESSION_KEY] = lang_code
            
            # Translate the URL if possible
            if next_url:
                translated_url = translate_url(next_url, lang_code)
                return HttpResponseRedirect(translated_url)
            
            # Fallback to the referrer or home page
            referer = request.META.get('HTTP_REFERER')
            if referer:
                translated_url = translate_url(referer, lang_code)
                return HttpResponseRedirect(translated_url)
            
            return HttpResponseRedirect('/')
    
    # If anything fails, redirect to the same page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))