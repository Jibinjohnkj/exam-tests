from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPES = (
        ('S', 'Student'),
        ('T', 'Teacher'),
    )
    type = models.CharField(choices=USER_TYPES, max_length=4)
