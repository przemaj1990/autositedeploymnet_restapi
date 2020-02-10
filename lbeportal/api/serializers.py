from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)

from lbeportal.models import SiteVendor
from accounts.api.serializers import UserDetailSerializer

class SiteVendorSerializer(ModelSerializer):
    class Meta:
        model = SiteVendor
        fields = '__all__'


class SiteVendorDetailSerializer(ModelSerializer):
    # user = SerializerMethodField()
    user = UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='lbeportal-api:delete',
        lookup_field='pk'
    )
    update_url = HyperlinkedIdentityField(
        view_name='lbeportal-api:update',
        lookup_field='pk'
    )
    # def get_user(self, obj):
    #     return str(obj.user.username)

    class Meta:
        model = SiteVendor
        # image = SerializerMethodField()
        html = SerializerMethodField()
        fields = [
            'site_code',
            'delivery_type',
            'address',
            'bandwidth',
            'site_classification',
            'delete_url',
            'update_url',
            'user',
            'get_api_url',
        ]
        read_only_fields = [
            'site_code',
            'user',
            'get_api_url',
        ]


        # def get_html(self, obj):
        #     return obj.get_markdown()

        # def get_image(self, obj):
        #     try:
        #         image = obj.image.url
        #     except:
        #         image = None
        #     return image

class SiteVendorListSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    # user = SerializerMethodField()
    url = HyperlinkedIdentityField(
        view_name='lbeportal-api:detail',
        lookup_field='pk'
    )
    delete_url = HyperlinkedIdentityField(
        view_name='lbeportal-api:delete',
        lookup_field='pk'
    )
    update_url = HyperlinkedIdentityField(
        view_name='lbeportal-api:update',
        lookup_field='pk'
    )
    def get_user(self, obj):
        return str(obj.user.username)

    class Meta:
        model = SiteVendor
        fields = [
            'url',
            'delete_url',
            'update_url',
            'site_code',
            'delivery_type',
            'address',
            'bandwidth',
            'site_classification',
            'user'
        ]

