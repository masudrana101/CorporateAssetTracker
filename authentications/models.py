from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.

class UserAccount(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email','phone']

    def __str__(self):
        return self.username
