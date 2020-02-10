from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    EmailField, CharField,
    HyperlinkedIdentityField,
    SerializerMethodField
)
from django.db.models import Q

User = get_user_model()

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]



class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email address')
    email2 = EmailField(label='Confirm email')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]
        extra_kwargs = {'password':
                            {'write_only': True}
                        }
    def validate(self, data):
        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exist():
            raise ValidationError('User already exist!')
        return data

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = data.get('email2')
        if email1 != email2:
            raise ValidationError('Email must match!')
        return value


    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    email = EmailField(label='Email Address', allow_blank=True, required=False)
    username = CharField(allow_blank=True, label='Username', required=False)
    token = CharField(allow_blank=True, read_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
        ]
        extra_kwargs = {'password':
                            {'write_only': True}
                        }
    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)
        password = data['password']
        if not email and not username:
            raise ValidationError('Lack of email or username')
        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exist() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('Username/email already in use')
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Incorrect credentials please try again')

        data['token'] = 'SOME RANDOM TOKEN'
        return data