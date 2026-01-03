from django.shortcuts import render, redirect
from .models import Lead

def landing_mafc(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        sex = request.POST.get('sex')
        location = request.POST.get('location')
        job = request.POST.get('job')

        # Validate tối thiểu
        if not full_name or not phone:
            return render(request, 'leads/landing_mafc.html', {
                'error': 'Vui lòng nhập đầy đủ họ tên và số điện thoại'
            })

        # Lưu DB
        Lead.objects.create(
            full_name=full_name,
            phone=phone,
            sex=sex,
            location=location,
            job=job
        )

        # 🔥 REDIRECT CHUẨN – KHÔNG 404
        return redirect('success')

    return render(request, 'leads/landing_mafc.html')


def success(request):
    return render(request, 'leads/landing_success.html')
