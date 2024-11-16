
from .models import Product

def categories_processor(request):
    """
    Context processor to make categories globally available.
    """
    categories = Product.objects.values_list('categoryName', flat=True).distinct()
    return {
        'categories': categories,
        'selected_category': request.GET.get('category', '').strip()
    }
