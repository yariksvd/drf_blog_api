from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth import get_user_model 
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Like(models.Model):
    user = models.ForeignKey(get_user_model(),
                            related_name='likes',
                            on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = ContentType('content_type', 'object_id')

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.title
    
    @property
    def total_likes(self):
        return self.likes.count()