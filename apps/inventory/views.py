from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Inventory
from .serializers import InventorySerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all().select_related("merchant", "center", "product")
    serializer_class = InventorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["product__name", "center__name"]
    ordering_fields = ["quantity", "updated_at"]

    # Optional filtering
    def get_queryset(self):
        qs = super().get_queryset()
        merchant = self.request.query_params.get("merchant")
        center = self.request.query_params.get("center")
        product = self.request.query_params.get("product")
        low_stock = self.request.query_params.get("low_stock")

        if merchant:
            qs = qs.filter(merchant_id=merchant)
        if center:
            qs = qs.filter(center_id=center)
        if product:
            qs = qs.filter(product_id=product)
        if low_stock:
            qs = qs.filter(quantity__lte=models.F("low_stock_threshold"))

        return qs

    # Custom endpoint: reduce quantity (used when placing orders)
    @action(detail=True, methods=["post"])
    def reduce(self, request, pk=None):
        inventory = self.get_object()
        qty = int(request.data.get("qty", 0))

        if qty <= 0:
            return Response({"error": "Invalid quantity"}, status=400)

        if inventory.quantity < qty:
            return Response({"error": "Insufficient stock"}, status=400)

        inventory.quantity -= qty
        inventory.save()

        return Response({"message": "Stock updated", "remaining": inventory.quantity})
