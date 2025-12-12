from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "merchant",
            "name",
            "description",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    center_name = serializers.CharField(source="center.name", read_only=True)
    merchant_name = serializers.CharField(source="merchant.username", read_only=True)  # changed from .name

    class Meta:
        model = Product
        fields = [
            "id",
            "merchant",
            "merchant_name",
            "center",
            "center_name",
            "category",
            "category_name",
            "name",
            "description",
            "price",
            "active",
            "image",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
