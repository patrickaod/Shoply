from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from django.contrib import messages
from user_activity.models import RecentlyViewedProduct

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

    if request.user.is_authenticated:
        # Save or update recently viewed product for logged-in users
        recently_viewed, created = RecentlyViewedProduct.objects.get_or_create(
            user=request.user,
            product=product
        )
        if not created:
            recently_viewed.save()  # Update timestamp
    else:
        # Use session for anonymous users
        recently_viewed = request.session.get('recently_viewed', [])
        if product_id not in recently_viewed:
            recently_viewed.append(product_id)
            # Limit to the last 10 items
            recently_viewed = recently_viewed[-10:]
            request.session['recently_viewed'] = recently_viewed

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_products.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'products/edit_products.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))