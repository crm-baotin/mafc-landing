from django.shortcuts import render, redirect
from .models import Lead


def landing(request):
    return render(request, 'leads/landing_mafc.html')


def submit(request):
    if request.method == 'POST':
        Lead.objects.create(
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            location=request.POST.get('location'),
            job=request.POST.get('job'),
        )
        return redirect('/success/')

    return redirect('/')


def success(request):
    return render(request, 'leads/success.html')
