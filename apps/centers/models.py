from django.db import models
from apps.merchants.models import Merchant

class Center(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='centers')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.merchant.name})"
