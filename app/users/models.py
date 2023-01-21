"""
Models for the User Class.
"""
from django.db import models


# Create your models here.
class User(models.Model):
    """
    Model for the Authentication User
    """
    email = models.EmailField()
    password = models.CharField(max_length=256)
