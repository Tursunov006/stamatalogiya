from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'amount', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('appointment__patient__first_name', 'appointment__doctor__first_name', 'transaction_id')
