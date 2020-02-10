from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import AccountsCreateAPIView, UserLoginAPIView


urlpatterns = [
    path('register/', AccountsCreateAPIView.as_view(), name='create'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
]