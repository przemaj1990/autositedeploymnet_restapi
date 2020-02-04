from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from engineers.api.views import (
    CommentsListAPIView, CommentsDetailAPIView
)

urlpatterns = [
    # path('', MainView.as_view(), name='main'),
    path('<int:pk>/', CommentsDetailAPIView.as_view(), name='detail'),
    path('list/', CommentsListAPIView.as_view(), name='list'),
]