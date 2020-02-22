import json
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

class PostsAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = get_user_model().objects.create_user(username="testuser", password='test')
        
        self.post = Post.objects.create(title="Test", body="Hello", author=self.user)
    
    def test_can_get_posts_list_if_logged_in(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('posts-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_get_posts_list_if_not_logged_in(self):
        response = self.client.get(reverse('posts-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_get_post_detail_if_logged_in(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('posts-detail', args=(self.post.pk,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_get_post_detail_if_not_logged_in(self):
        response = self.client.get(reverse('posts-detail', args=(self.post.pk,)))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_create_post_if_logged_in(self):
        self.client.force_authenticate(user=self.user)
        params = {
            "title": "test1",
            "body": "Hi"}
        response = self.client.post(reverse('posts-list'), params)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_cannot_create_post_if_not_logged_in(self):
        params = {
            "title": "test1",
            "body": "Hi"}
        response = self.client.post(reverse('posts-list'), params)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_can_like_if_logged_in(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('posts-like', args=(self.post.pk,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_can_unlike_if_logged_in(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('posts-like', args=(self.post.pk,)))
        response1 = self.client.post(reverse('posts-unlike', args=(self.post.pk,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
    
    def test_cannot_like_if_is_liked_true(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('posts-like', args=(self.post.pk,)))
        response1 = self.client.post(reverse('posts-like', args=(self.post.pk,)))        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_unlike_if_is_liked_false(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('posts-unlike', args=(self.post.pk,)))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_cannot_like_if_not_logged_in(self):
        response = self.client.post(reverse('posts-like', args=(self.post.pk,)))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_cannot_unlike_if_not_logged_in(self):
        response = self.client.post(reverse('posts-unlike', args=(self.post.pk,)))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)