from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Product, Category,Review
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def product_list(request):
    """Display all products with advanced filtering"""
    products = Product.objects.filter(is_active=True).select_related('category')
    categories = Category.objects.all()
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(composition__icontains=query) |
            Q(benefits__icontains=query) |
            Q(category__name__icontains=query)
        )
    
    # Filters
    filters = {
        'category': request.GET.get('category'),
        'strain_type': request.GET.getlist('strain'),
        'ratio': request.GET.get('ratio'),
        'min_price': request.GET.get('min_price'),
        'max_price': request.GET.get('max_price'),
        'method': request.GET.getlist('method')
    }
    
    # Apply filters
    if filters['category']:
        products = products.filter(category__slug=filters['category'])
    
    if filters['strain_type']:
        products = products.filter(strain_type__in=filters['strain_type'])
    
    if filters['ratio']:
        products = products.filter(preferred_ratio=filters['ratio'])
    
    if filters['min_price']:
        products = products.filter(price__gte=filters['min_price'])
    
    if filters['max_price']:
        products = products.filter(price__lte=filters['max_price'])
    
    if filters['method']:
        products = products.filter(recommended_methods__overlap=filters['method'])
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    category = None
    if filters['category']:
        try:
            category = Category.objects.get(slug=filters['category'])
        except Category.DoesNotExist:
            pass

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'category': category,
        'query': query,
        'filters': filters,
        'strain_choices': Category.STRAIN_TYPE_CHOICES,
        'ratio_choices': Category.RATIO_CHOICES,
        'method_choices': Category.CONSUMPTION_METHODS,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, slug):
    """Display product detail page with all information"""
    product = get_object_or_404(
        Product.objects.select_related('category'),
        slug=slug,
        is_active=True
    )
    
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)

def category_detail(request, slug):
    """Display products in a specific category with applied filters"""
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_active=True)

    # Price filter
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Strain type filter
    strain_type = request.GET.get('strain_type')
    if strain_type:
        products = products.filter(strain_type=strain_type)

    # Ratio filter
    ratio = request.GET.get('ratio')
    if ratio:
        products = products.filter(preferred_ratio=ratio)

    # Consumption method filter
    methods = request.GET.getlist('method')
    if methods:
        products = products.filter(recommended_methods__overlap=methods)

    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'page_obj': page_obj,
        'min_price': min_price,
        'max_price': max_price,
        'active_filters': {
            'strain_type': strain_type,
            'ratio': ratio,
            'methods': methods,
        },
        'strain_choices': Category.STRAIN_TYPE_CHOICES,
        'ratio_choices': Category.RATIO_CHOICES,
        'method_choices': Category.CONSUMPTION_METHODS,
        'request': request,  # Make sure request is in context
    }
    return render(request, 'products/category_detail.html', context)

    # views.py

@login_required
@require_POST
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Check if user already reviewed this product
    existing_review = Review.objects.filter(product=product, user=request.user).first()
    
    try:
        rating = int(request.POST.get('rating', 0))
        comment = request.POST.get('comment', '').strip()
        
        # Validate rating
        if not 0 <= rating <= 5:
            raise ValueError("Rating must be between 0 and 5")
            
        # # Validate comment
        # if not comment:
        #     raise ValueError("Comment cannot be empty")
            
        # Update or create review
        if existing_review:
            # Update existing review
            existing_review.rating = rating
            existing_review.comment = comment
            existing_review.save()
            
            # We need to recalculate the average rating since an existing review was updated
            reviews = product.reviews.all()
            if reviews.exists():
                total_ratings = sum(review.rating for review in reviews)
                product.rating_count = reviews.count()
                product.average_rating = total_ratings / product.rating_count
                product.save()
                
            messages.success(request, "Your review has been updated.")
        else:
            # Create new review
            Review.objects.create(
                product=product,
                user=request.user,
                rating=rating,
                comment=comment
            )
            
            # Update product rating stats
            product.update_rating(rating)
            messages.success(request, "Thank you for your review!")
            
    except ValueError as e:
        messages.error(request, str(e))
    except Exception as e:
        messages.error(request, "An error occurred while submitting your review.")
        
    return redirect(product.get_absolute_url())

