from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    # ASIN (Amazon Standard Identification Number)
    asin = models.CharField(max_length=100, unique=True)
    
    # Product title
    title = models.CharField(max_length=255)
    
    # Image URL (URL to the product image)
    imgUrl = models.URLField(max_length=200)
    
    # Product URL (URL to the product page)
    productURL = models.URLField(max_length=200)
    
    # Rating of the product (e.g., stars out of 5)
    stars = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True, 
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )

    # Number of reviews for the product
    reviews = models.IntegerField(null=True, blank=True)
    
    # Price of the product
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    
    # Whether or not the product is a bestseller
    isBestSeller = models.BooleanField(default=False)
    
    # Whether the product was bought in the last month
    boughtInLastMonth = models.BooleanField(default=False)
    
    # Category of the product (e.g., Electronics, Clothing, etc.)
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.title