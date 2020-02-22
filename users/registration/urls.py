from django.conf.urls import url

from .views import UserRegisterView

urlpatterns = [
    url('', UserRegisterView.as_view(), name='register'),
]