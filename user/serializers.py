from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','first_name', 'last_name','gender', 'email', 'birthday', 'password', 'profile_pic', 'cover_pic', 'is_verified']


class ChatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name']


class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()