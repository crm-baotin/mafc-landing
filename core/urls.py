from django.contrib import admin
from django.urls import path, include
from leads import views

urlpatterns = [
    path('', views.landing_mafc, name='home'),  # 👈 ROOT
    path('mafc/', include('leads.urls')),       # vẫn giữ nếu cần
    path('admin/', admin.site.urls),
]
