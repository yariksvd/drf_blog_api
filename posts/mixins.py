from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from .exceptions import (AlreadyLiked, NotLikedYet)

from . import services


class LikedMixin:
    
    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        obj = self.get_object()
        if services.is_liked(obj, request.user):
            raise AlreadyLiked()
        services.add_like(obj, request.user)
        return Response()
    
    @action(methods=['POST'], detail=True)
    def unlike(self, request, pk=None):
        obj = self.get_object()
        if not services.is_liked(obj, request.user):
            raise NotLikedYet()
        services.remove_like(obj, request.user)
        return Response()
