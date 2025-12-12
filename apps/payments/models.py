from django.db import models
from apps.orders.models import Order
from apps.users.models import User

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50, default='cash')
    created_at = models.DateTimeField(auto_now_add=True)
