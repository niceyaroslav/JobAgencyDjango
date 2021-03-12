from django.views.generic import View, TemplateView, CreateView
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


class MainMenuView(CreateView):
    template_name = "first_page/menu.html"

    def get_context_data(self, **kwargs):
        return {"data": {"Login page": 'login',
                         "Sign up page": 'signup',
                         "Vacancy list": 'vacancies',
                         "Resume list": 'resumes',
                         "Personal profile": 'home'}}


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'first_page/login.html'


class MySingUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'first_page/signup.html'


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, template_name='first_page/home.html')
        else:
            return redirect('/')





