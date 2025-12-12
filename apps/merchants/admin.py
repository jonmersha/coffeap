from django.contrib import admin
from .models import Merchant

@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'contact_email', 'contact_phone', 'created_at')
    search_fields = ('name', 'owner__username', 'contact_email')
    list_filter = ('created_at',)
