from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'asin',
        'title',
        'categoryName',
        'price',
        'stars',
        'isBestSeller',
        'imgUrl',
    )

    ordering = ('title',)
    
admin.site.register(Product, ProductAdmin)