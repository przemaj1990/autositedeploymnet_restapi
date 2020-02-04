from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from lbeportal.views import SiteVendorCreateView, SiteVendorDetailView, SiteVendorListView, SiteVendorUpdateView, \
    SiteVendorDeleteView, MainView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('create/', SiteVendorCreateView.as_view(), name='create'),
    path('<int:pk>/', SiteVendorDetailView.as_view(), name='detail'),
    path('list/', SiteVendorListView.as_view(), name='list'),
    path('update/<int:pk>', SiteVendorUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', SiteVendorDeleteView.as_view(), name='delete')
]