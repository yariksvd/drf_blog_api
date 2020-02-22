from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

class AuthAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.data = {"username": "testuser", "password": "test"}
        self.user = get_user_model().objects.create_user(username="testuser", password="test")
        response = self.client.post(reverse("rest_login"), self.data, format="json")
        self.token = response.data["token"]

    def test_user_jwt_token_login(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get(reverse("posts-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_can_register_if_email_is_verified(self):
        data = {
            "username": "testuser1", 
            "password1": "ASDzxc456", 
            "password2": "ASDzxc456", 
            "email": "hello@weareclario.com", 
        }
        response = self.client.post(reverse('register'), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.content)
    
    def test_user_can_register_if_email_is_not_verified(self):
        data = {
            "username": "testuser1", 
            "password1": "ASDzxc456", 
            "password2": "ASDzxc456", 
            "email": "test@test.com", 
        }
        response = self.client.post(reverse('register'), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.content)