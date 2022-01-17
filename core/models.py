from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', null=True, blank=True)


class Profile(models.Model):
    name = models.CharField(max_length=225)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)