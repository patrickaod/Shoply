from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product


def product_search(request):
    """
    View for searching and filtering products based on category or search query.
    """
    # Base queryset
    products = Product.objects.all()

    # Get distinct categories for dropdown
    categories = Product.objects.values_list('categoryName', flat=True).distinct()

    # Get query parameters
    category = request.GET.get('category', '').strip()
    query = request.GET.get('q', '').strip()

    # Initialize filters
    filters = Q()
    if category:
        filters &= Q(categoryName=category)  # Filter by category
    if query:
        filters &= Q(title__icontains=query) | Q(categoryName__icontains=query)  # Filter by title

    # Fetch filtered products
    products = Product.objects.filter(filters)

    context = {
        'categories': categories,
        'products': products,
        'selected_category': category,
        'search_query': query,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
