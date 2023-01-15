"""
Test cases for the Home View.
"""
from django.test import SimpleTestCase
from django.http import HttpRequest
from rest_framework import status
from core import views


class TestViews(SimpleTestCase):
    """
    Test cases for the views class of the core app.
    """
    def setUp(self):
        """Set up the initial information for test cases."""
        self.home_view = views.HomeView.as_view()

    def test_request_home_view(self):
        request = HttpRequest()
        request.method = 'GET'
        request.META['SERVER_NAME'] = 'localhost'
        response = self.home_view(request)
        response_title = response.content.decode(
            'utf-8').split('<title>')[1].split('</title>')[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response_title,
            'Home'
        )
