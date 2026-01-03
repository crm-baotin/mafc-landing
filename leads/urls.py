from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_mafc, name='landing_mafc'),
    path('success/', views.success, name='success'),
]
