from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'active')
    list_filter = ('specialization', 'active')
    search_fields = ('first_name', 'last_name', 'specialization')
