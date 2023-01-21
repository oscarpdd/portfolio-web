"""
Views of the Users app.
"""
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from users import forms


# Create your views here.
class LoginUserView(LoginView):
    """
    Login View for a user.
    """
    app_name = 'users'
    page_name = 'users'
    template_name = f'{app_name}/login.html'
    success_url = reverse_lazy('my_profile')
    form_class = forms.LoginForm

    def get(self, request, *args, **kwargs):
        context = {'valid_form': True,
                   'app_name': self.app_name,
                   'page_name': self.page_name}
        return render(request, template_name=self.template_name,
                      context=context)

    def post(self, request, *args, **kwargs):
        login_form = self.form_class(request.POST)
        context = {'valid_form': login_form.is_valid(),
                   'app_name': self.app_name,
                   'page_name': self.page_name}
        if context['valid_form']:
            # TODO: Login here.
            return HttpResponseRedirect(self.success_url)
        return render(request, template_name=self.template_name,
                      context=context)


class MyProfileView(FormView):
    """
    My Profile View, where the user can update his personal data.
    """
    app_name = 'users'
    page_name = 'users'
    template_name = f'{app_name}/my_profile.html'

    def get(self, request, *args, **kwargs):
        context = {'app_name': self.app_name,
                   'page_name': self.page_name}
        return render(request, template_name=self.template_name,
                      context=context)
