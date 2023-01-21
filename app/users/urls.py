"""
URLs for the Users app,
it contains the Login/Logout/Register/etc functionality.
"""
from django.urls import re_path
from users import views

urlpatterns = [
    re_path(r'^(?P<app>[a-z]+)/login$',
            views.LoginUserView.as_view(), name='login'),
    re_path(r'^(?P<app>[a-z]+)/my_profile',
            views.MyProfileView.as_view(), name='my_profile'),
    re_path(r'^(?P<app>[a-z]+)$',
            views.LoginUserView.as_view(), name='users_home')
]
