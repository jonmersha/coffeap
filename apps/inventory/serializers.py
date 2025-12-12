from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    center_name = serializers.CharField(source="center.name", read_only=True)
    merchant_name = serializers.CharField(source="merchant.name", read_only=True)

    class Meta:
        model = Inventory
        fields = [
            "id",
            "merchant",
            "merchant_name",
            "center",
            "center_name",
            "product",
            "product_name",
            "quantity",
            "low_stock_threshold",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")
