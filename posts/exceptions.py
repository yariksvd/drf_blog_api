from rest_framework.exceptions import APIException
from rest_framework import status

class AlreadyLiked(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'User already liked this post.'
    default_code = 'liked'

class NotLikedYet(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'User not liked this post yet.'
    default_code = 'notliked'
    