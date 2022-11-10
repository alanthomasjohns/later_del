from django import views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('verify_otp/', VerifyOTP.as_view()),
    path('login/', LoginAPI.as_view()),
]