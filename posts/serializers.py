from rest_framework import serializers
from django.contrib.auth import get_user_model 

from . import services as likes_services
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'body',
            'created_at',
            'total_likes',
            'is_liked',
        )
    def get_is_liked(self, obj) -> bool:
        user = self.context.get('request').user
        return likes_services.is_liked(obj, user)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')