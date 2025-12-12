from django.db import models
from django.utils import timezone
from apps.centers.models import Center
from apps.merchants.models import Merchant   # adjust import paths if needed


class Category(models.Model):
    merchant = models.ForeignKey(
        Merchant,
        on_delete=models.CASCADE,
        related_name="categories",
        help_text="Each merchant has their own categories."
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("merchant", "name")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.merchant.name})"


class Product(models.Model):
    merchant = models.ForeignKey(
        Merchant,
        on_delete=models.CASCADE,
        related_name="products",
    )
    center = models.ForeignKey(
        Center,
        on_delete=models.CASCADE,
        related_name="products",
        help_text="Product available in this specific center."
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="products",
    )

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    active = models.BooleanField(default=True)

    # optional features
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        unique_together = ("merchant", "center", "name")

    def __str__(self):
        return f"{self.name} - {self.center.name}"
