from rest_framework.viewsets import ModelViewSet
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all().order_by("-created_at")
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Clients see only their orders
        if self.request.user.role == "client":
            return Order.objects.filter(user=self.request.user)
        return Order.objects.all()
