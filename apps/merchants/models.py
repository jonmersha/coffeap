from django.db import models
from apps.users.models import User

class Merchant(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="merchant_profile")
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
