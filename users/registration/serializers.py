from rest_auth.registration.serializers import RegisterSerializer

from rest_framework import serializers

from .validators import email_exists

class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(validators=[email_exists])