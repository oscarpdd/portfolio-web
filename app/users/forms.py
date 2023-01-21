"""
Form classes for users (Login, My Profile).
"""
from django import forms
from users import models


class LoginForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['email', 'password']

    remember_me = forms.BooleanField(label='remember_me')
