from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from users.validators import validate_username, validate_password
from users.models import User


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'is_staff',
                  'is_active',
                  'date_joined')


class CustomUserCreateSerializer(UserCreateSerializer):

    class Meta:
        model = User
        fields = User.REQUIRED_FIELDS

    def validate_username(self, value):
        return validate_username(value)

    def validate_password(self, value):
        return validate_password(value)
