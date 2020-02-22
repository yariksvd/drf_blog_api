import os

from allauth.account.adapter import get_adapter

from rest_framework import serializers

from .hunter_checker import HunterEmail

hunter = HunterEmail(os.environ['HUNTER_API_KEY'])

def email_exists(email):
    
    if hunter.email_verifier(email) != "deliverable":
        raise serializers.ValidationError("Email is not deliverable.")
    return email
