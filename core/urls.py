from django.contrib import admin
from django.urls import path
from leads import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.landing, name='landing'),
    path('submit/', views.submit, name='submit'),
    path('success/', views.success, name='success'),
]
