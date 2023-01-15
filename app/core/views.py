"""
Views of the core app.
"""
from django.views.generic import View
from django.shortcuts import render


class HomeView(View):
    template_name = 'core/home.html'

    def get(self, request):
        """
        GET method of the Home View.
        """
        return render(request=request, template_name=self.template_name,
                      context={})
