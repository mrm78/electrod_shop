from django.db import models
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = " کاربر"

