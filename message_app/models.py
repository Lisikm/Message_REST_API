from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    content = models.CharField(max_length=160)
    display_count = models.IntegerField(default=0)


User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False
