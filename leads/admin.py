from django.contrib import admin
from .models import Lead
from .admin_filters import CreatedAtRangeFilter
from .admin_actions import export_leads_excel


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

    list_filter = (
        CreatedAtRangeFilter,   # 👈 lọc hôm nay / 7 ngày / 30 ngày
        "sex",
        "location",
        "job",
        "created_at",           # 👈 filter theo khoảng ngày (calendar)
    )

    actions = [export_leads_excel]  # 👈 export Excel

    ordering = ("-created_at",)
    list_per_page = 25
