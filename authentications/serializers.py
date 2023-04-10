from rest_framework import serializers
from .models import UserAccount as User
from rest_framework_simplejwt.tokens import RefreshToken



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['id', 'is_admin']


class UserTokenSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'first_name', 'last_name', 'password', 'token', 'is_admin']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['id', 'is_admin']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class LogSerializer(serializers.Serializer):
    phone_or_email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'first_name', 'last_name']
        read_only_fields = ['id']

class PasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=100)
    new_password = serializers.CharField(max_length=100)
