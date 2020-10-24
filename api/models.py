from django.db import models

from rest_framework.authtoken.models import Token

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings

def token_request(request):
    if user_requested_token() and token_request_is_warranted():
        new_token = Token.objects.create(user=request.user)@receiver(post_save, sender=settings.AUTH_USER_MODEL)
        
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)