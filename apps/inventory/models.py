from django.db import models
from apps.merchants.models import Merchant
from apps.centers.models import Center
from apps.products.models import Product

class Inventory(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="inventory")
    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name="inventory")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="inventory_items")
    quantity = models.PositiveIntegerField(default=0)
    low_stock_threshold = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("merchant", "center", "product")

    def __str__(self):
        return f"{self.product.name} - {self.center.name} ({self.quantity})"
