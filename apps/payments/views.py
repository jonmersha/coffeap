from rest_framework.viewsets import ModelViewSet
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework.permissions import IsAuthenticated

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
