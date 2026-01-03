from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import Lead


def landing_mafc(request):
    if request.method == "POST":
        phone = request.POST.get("phone")

        # ===== CHỐNG SPAM: 10 PHÚT / 1 SỐ =====
        limit_time = timezone.now() - timedelta(minutes=10)
        if Lead.objects.filter(phone=phone, created_at__gte=limit_time).exists():
            return render(request, "leads/landing_mafc.html", {
                "error": "Số điện thoại này vừa gửi thông tin. Vui lòng thử lại sau ít phút."
            })

        # ===== LƯU LEAD =====
        Lead.objects.create(
            full_name=request.POST.get("full_name"),
            phone=phone,
            sex=request.POST.get("sex"),
            location=request.POST.get("location"),
            job=request.POST.get("job"),
        )

        return redirect("/mafc/success/")

    return render(request, "leads/landing_mafc.html")


def success(request):
    return render(request, "leads/landing_success.html")
