from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'phone',
        'location',
        'job',
        'created_at',
    )

    list_filter = (
        'location',
        'job',
    )

    search_fields = (
        'full_name',
        'phone',
    )

    ordering = ('-created_at',)
