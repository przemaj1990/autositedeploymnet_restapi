from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView
)
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
from django.db.models import Q
from lbeportal.api.permissions import IsOwnerOrReadOnly
from lbeportal.models import SiteVendor
from lbeportal.api.serializers import SiteVendorSerializer, SiteVendorDetailSerializer, SiteVendorListSerializer

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import UserCreateSerializer, UserLoginSerializer
from lbeportal.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination
from django.contrib.auth import get_user_model
User = get_user_model()


class AccountsCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    model = User.objects.all()

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



