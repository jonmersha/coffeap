from rest_framework import viewsets, permissions

from apps.merchants.models import Merchant
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class MerchantFilteredQuerysetMixin:
    """
    Ensures merchants can access only their own data.
    """

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return self.queryset.none()
        
        # Access the merchant profile
        try:
            merchant = user.merchant_profile  # matches related_name in Merchant model
        except Merchant.DoesNotExist:
            return self.queryset.none()
        
        return self.queryset.filter(merchant=merchant)

    def perform_create(self, serializer):
        try:
            merchant = self.request.user.merchant_profile
        except Merchant.DoesNotExist:
            raise PermissionError("User does not have a merchant profile")
        serializer.save(merchant=merchant)


class CategoryViewSet(MerchantFilteredQuerysetMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(MerchantFilteredQuerysetMixin, viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category", "center", "merchant")
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]