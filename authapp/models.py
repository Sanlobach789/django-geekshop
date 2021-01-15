from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.utils.timezone import now


class User(AbstractUser):
    extra_avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        return True
