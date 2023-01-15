"""
URLs for the core app, it contains the home page.
"""
from django.urls import path
from core import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]
