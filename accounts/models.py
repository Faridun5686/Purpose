from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Customer', 'Customer'),
        ('Manager', 'Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Customer')
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
