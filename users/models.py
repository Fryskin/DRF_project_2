from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone_number = models.CharField(max_length=20, verbose_name='phone_number', **NULLABLE)
    city = models.CharField(max_length=92, verbose_name='city', **NULLABLE)
    preview = models.ImageField(upload_to='images/users/', verbose_name='preview', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

