from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "created_at")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "price",
        "active",
        "created_at",
        "updated_at",
    )

    list_filter = ("category", "active")
    search_fields = ("name",)
    ordering = ("name",)

    readonly_fields = ("created_at", "updated_at")
