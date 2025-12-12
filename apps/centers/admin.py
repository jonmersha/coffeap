from django.contrib import admin
from .models import Center

@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'merchant', 'location', 'is_active')
    search_fields = ('name', 'merchant__name', 'location')
    list_filter = ('is_active', 'merchant')
