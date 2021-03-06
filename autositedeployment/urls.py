"""autositedeployment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token

from engineers.views import (login_view, register_view, logout_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lbe_portal/', include(('lbeportal.urls', 'lbeportal'), namespace='lbeportal')),
    # api for lbeportal:
    path('api/lbe_portal/', include(('lbeportal.api.urls', 'lbeportal'), namespace='lbeportal-api')),
    # api for accounts:
    path('api/accounts/', include(('accounts.api.urls', 'accounts'), namespace='accounts')),
    # path('', include('django.contrib.auth.urls')),
    # api for engineers:
    path('api/engineers/', include(('engineers.api.urls', 'engineers'), namespace='engineers-api')),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('api-token-auth/', obtain_jwt_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




