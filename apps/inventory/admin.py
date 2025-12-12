from django.contrib import admin
from .models import Inventory

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "merchant",
        "center",
        "quantity",
        "low_stock_threshold",
        "is_low",  # define this as method below
        "updated_at",
    )
    list_filter = ("merchant", "center")
    search_fields = ("product__name",)

    def is_low(self, obj):
        return obj.quantity <= obj.low_stock_threshold
    is_low.boolean = True  # shows a green/red icon in admin
    is_low.short_description = "Low Stock"
