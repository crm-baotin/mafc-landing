from django.shortcuts import render, redirect
from .models import Lead
from .telegram import send_telegram
from django.utils import timezone



def landing(request):
    return render(request, 'leads/landing_mafc.html')


from django.shortcuts import redirect
from django.utils import timezone
from datetime import timedelta
from .models import Lead
from .telegram import send_telegram


def submit(request):
    if request.method == 'POST':

        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        job = request.POST.get('job')

        # ===== CHỐNG SPAM SĐT (HQA) =====
        time_limit = timezone.now() - timedelta(hours=24)

        count = Lead.objects.filter(
            phone=phone,
            created_at__gte=time_limit
        ).count()

        if count >= 2:
            # ❗ TRẢ VỀ LANDING + CẢNH BÁO
            return render(
                request,
                'leads/landing_mafc.html',
                {
                    'spam_warning': 'Số điện thoại này đã gửi yêu cầu nhiều lần trong hôm nay. Vui lòng chờ hoặc liên hệ trực tiếp để được hỗ trợ.'
                }
            )

        # ===== LƯU LEAD =====
        Lead.objects.create(
            full_name=full_name,
            phone=phone,
            location=location,
            job=job,
        )

        # ===== GỬI TELE =====
        from .telegram import send_telegram
        now_time = timezone.localtime().strftime("%H:%M – %d/%m/%Y")

        msg = f"""
📥 <b>LEAD MỚI – MAFC</b>

👤 Họ tên: {full_name}
📞 SĐT: {phone}
📍 Khu vực: {location}
💼 Nghề nghiệp: {job}

⏰ Thời gian: {now_time}
🌐 Nguồn: MAFC Landing
        """

        send_telegram(msg)

        return redirect('/success/')

    return redirect('/')




def success(request):
    return render(request, 'leads/success.html')

