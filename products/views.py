from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_search(request):
    """
    View for searching and filtering products based on category or search query.
    """
    # Base queryset
    products = Product.objects.all()

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
        'products': products,
        'selected_category': category,
        'search_query': query,
    }
    return render(request, 'products/products.html', context)
