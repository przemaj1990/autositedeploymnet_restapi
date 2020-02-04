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

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )
from django.db.models import Q
from lbeportal.api.permissions import IsOwnerOrReadOnly
from engineers.models import Comments
from .serializers import CommentsSerializer
from lbeportal.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination


















class CommentsListAPIView(ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user', 'content']
    # pagination_class = PostLimitOffsetPagination
    pagination_class = PostPageNumberPagination

    # lookup_field = 'site_code'
    # permission_classes = [IsOwnerOrReadOnly]

    # def get_queryset(self, *args, **kwargs):
    #     # queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
    #     queryset_list = SiteVendor.objects.all()  # filter(user=self.request.user)
    #     query = self.request.GET.get("q")
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(site_code__icontains=query) |
    #             Q(address__icontains=query) |
    #             Q(bandwidth__icontains=query) |
    #             Q(site_classification__icontains=query) |
    #             Q(user__first_name__icontains=query) |
    #             Q(user__last_name__icontains=query)
    #         ).distinct()
    #     return queryset_list


class CommentsDetailAPIView(RetrieveAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

# class SiteVendorUpdateAPIView(UpdateAPIView):
#     queryset = SiteVendor.objects.all()
#     serializer_class = SiteVendorSerializer
#     permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
#
#     def perform_update(self, serializer):
#         serializer.save(engineer=self.request.user)
#
# class SiteVendorDeleteAPIView(DestroyAPIView):
#     queryset = SiteVendor.objects.all()
#     serializer_class = SiteVendorDetailSerializer
#
# class SiteVendorCreateAPIView(CreateAPIView):
#     queryset = SiteVendor.objects.all()
#     serializer_class = SiteVendorDetailSerializer
#     permission_classes = [IsAuthenticated]
#
#
#     def perform_create(self, serializer):
#         serializer.save(engineer=self.request.user)