"""
Form classes for users (Login, My Profile).
"""
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django import forms
from users import models


class LoginForm(forms.ModelForm):
    remember_me = forms.BooleanField(label='remember_me')
    user_cache = None

    class Meta:
        model = models.User
        fields = ['email', 'password']

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        print(self.cleaned_data)
        if email is not None and password:
            self.user_cache = authenticate(
                email=email, password=password
            )
            if self.user_cache is None:
                raise ValidationError(
                    f'Invalid login: {email} is not registered.'
                )
            else:
                if not self.user_cache.is_active:
                    raise ValidationError(
                        'Invalid login: User is inactive.'
                    )
        return self.cleaned_data

    def get_user(self):
        return self.user_cache
