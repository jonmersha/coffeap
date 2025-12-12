from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'user', 'amount', 'method', 'created_at')
    search_fields = ('order__id', 'user__username', 'method')
    list_filter = ('method',)
