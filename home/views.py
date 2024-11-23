from django.shortcuts import render
from products.models import Product
from user_activity.models import RecentlyViewedProduct
import random


def index(request):
    """
    A view to return the index page
    """
    # Get all bestseller products
    bestseller_products = list(Product.objects.filter(isBestSeller=True))
    # Shuffle and pick up to 5
    trending_products = random.sample(
        bestseller_products,
        min(len(bestseller_products), 5)
        )

    # Fetch recently viewed products
    recently_viewed_products = []
    if request.user.is_authenticated:
        # For logged-in users: fetch from the database
        recent_views = (
            RecentlyViewedProduct.objects
            .filter(user=request.user)
            .select_related('product')[:10]
        )
        recently_viewed_products = [view.product for view in recent_views]
    else:
        # For anonymous users: fetch from session
        recently_viewed_ids = request.session.get('recently_viewed', [])
        recently_viewed_products = Product.objects.filter(
                id__in=recently_viewed_ids
            )

    # Randomly sample up to 5 recently viewed products
    recently_viewed_sample = random.sample(
        list(recently_viewed_products),
        min(len(recently_viewed_products), 4)
    )

    context = {
        'trending_products': trending_products,
        'recently_viewed_products': recently_viewed_sample,
    }

    return render(request, 'home/index.html', context)
