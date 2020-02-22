from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer
from .models import Post
from .mixins import LikedMixin

class PostViewSet(LikedMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)