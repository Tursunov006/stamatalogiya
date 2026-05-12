from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration_minutes', 'price', 'active')
    list_filter = ('active',)
    search_fields = ('title', 'description')
