from allauth.account import app_settings as allauth_settings
from rest_auth.registration.views import RegisterView
from rest_framework.response import Response


from .serializers import CustomRegisterSerializer

class UserRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer