from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from lbeportal.api.views import (
    SiteVendorListAPIView, SiteVendorDetailAPIView, SiteVendorUpdateAPIView, SiteVendorDeleteAPIView, SiteVendorCreateAPIView,
SiteVendorEditAPIView

)

urlpatterns = [
    # path('', MainView.as_view(), name='main'),
    path('create/', SiteVendorCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', SiteVendorDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/edit/', SiteVendorEditAPIView.as_view(), name='edit'),
    path('list/', SiteVendorListAPIView.as_view(), name='list'),
    path('update/<int:pk>', SiteVendorUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>', SiteVendorDeleteAPIView.as_view(), name='delete')
]