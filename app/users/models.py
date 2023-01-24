"""
Models for the User Class.
"""
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """
    Manager for users.
    """
    def create_user(self, email, password=None):
        """
        Create a new user.
        """
        # Checks email.
        if not email:
            raise ValueError('Users must have an email address.')
        email = self.normalize_email(email=email)

        # Create user.
        user = self.model(email=email)

        # Set password.
        user.set_password(raw_password=password)

        # Save the user.
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Create and save a new superuser with given details.
        """
        user = self.create_user(email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model for the User
    """
    # Database fields.
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Manager and configuration.
    objects = UserManager()
    USERNAME_FIELD = 'email'
