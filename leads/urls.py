from django.urls import path
from django.shortcuts import redirect
from .views import landing_mafc, success

urlpatterns = [
    path("", lambda request: redirect("/mafc/")),   # root → /mafc/
    path("mafc/", landing_mafc, name="landing_mafc"),
    path("mafc/success/", success, name="landing_success"),
]
