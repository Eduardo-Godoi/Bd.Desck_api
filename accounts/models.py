from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    address = models.OneToOneField('accounts.Address', on_delete=models.CASCADE, related_name='user')


class Address (models.Model):
    zip_code = models.CharField(max_length=255)
    public_area = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=3)
