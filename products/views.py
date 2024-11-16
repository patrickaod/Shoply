from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator

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

    # Paginate products (10 per page)
    paginator = Paginator(products,  10)
    page_number = request.GET.get('page')
    paginated_products = paginator.get_page(page_number)

    context = {
        'products': paginated_products,
        'selected_category': category,
        'search_query': query,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """
    A view to show individual product details
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)