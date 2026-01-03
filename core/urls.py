from django.contrib import admin
from django.urls import path, include
from leads import views

urlpatterns = [
    path('', views.landing_mafc, name='home'),     # Trang chủ
    path('mafc/', include('leads.urls')),          # App leads
    path('admin/', admin.site.urls),
]
