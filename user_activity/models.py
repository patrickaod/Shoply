from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class RecentlyViewedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-viewed_at']  # Latest views first

    def __str__(self):
        return f"{self.user.username} viewed {self.product.name}"
