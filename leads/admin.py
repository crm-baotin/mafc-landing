from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "phone",
        "sex",
        "location",
        "job",
        "created_at",
    )

    search_fields = ("full_name", "phone")
    list_filter = ("sex", "location", "job", "created_at")
    ordering = ("-created_at",)

    list_per_page = 20
