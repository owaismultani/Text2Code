# accounts/views.py
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import views as auth_views
from django.views.generic.edit import FormView
from django.contrib.auth.views import PasswordResetDoneView as AuthPasswordResetDoneView


class CustomLoginView(LoginView):
    """
    Custom login view to redirect authenticated users to the home page.
    """
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True  # Redirect users who are already logged in
    next_page = reverse_lazy('home')  # Redirect to this page after login, replace 'home' with your target view name


class SignUpView(CreateView):
    """
    Custom sign up view to redirect users to the login page after successful registration.
    """
    form_class = SignUpForm
    success_url = reverse_lazy('login')  # Redirect to the login page after successful registration
    template_name = 'accounts/signup.html'


class CustomLogoutView(View):
    """
    Custom logout view to redirect users to the logout page.
    """
    def post(self, request):
        logout(request)
        return render(request, 'accounts/logout.html')


class PasswordResetRequestView(FormView):
    """
    Custom password reset request view to redirect users to the password reset done page.
    """
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm

    def form_valid(self, form):
        opts = {
            'use_https': self.request.is_secure(),
            'token_generator': default_token_generator,
            'from_email': None,
            'email_template_name': 'accounts/password_reset_email.html',
            'subject_template_name': 'accounts/password_reset_subject.txt',
            'request': self.request,
            'html_email_template_name': None,
            'extra_email_context': None,
        }
        form.save(**opts)
        return super().form_valid(form)


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """
    Custom password reset confirm view to redirect users to the login page after successful password reset.
    """
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('login')
    form_class = SetPasswordForm


class PasswordResetDoneView(AuthPasswordResetDoneView):
    """
    Custom password reset done view to redirect users to the login page after successful password reset.
    """
    template_name = 'accounts/password_reset_done.html'
