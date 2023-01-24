"""
Views of the Users app.
"""
from django.contrib.auth import views as auth_views
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views.generic import FormView, View
from django.shortcuts import render
from django.urls import reverse_lazy
from users import forms


# Create your views here.
class LoginUserView(auth_views.LoginView):
    """
    Login View for a user.
    """
    app_name = 'users'
    page_name = 'users'
    template_name = f'{app_name}/login.html'
    success_url = reverse_lazy('my_profile',
                               kwargs={'app': app_name})
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
            if not login_form.cleaned_data.get('remember_me'):
                request.session.set_expiry(0)
            auth_login(request, login_form.get_user())
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


class LogoutView(View):
    """
    Logout View for a user.
    """
    app_name = 'users'
    page_name = 'users'
    success_url = reverse_lazy('login',
                               kwargs={'app': app_name})

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return HttpResponseRedirect(self.success_url)
