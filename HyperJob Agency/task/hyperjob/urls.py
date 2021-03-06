"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hyperjob.views import MainMenuView, HomeView, MyLoginView, MySingUpView
from vacancy.views import VacancyListView, AddVacancyView
from resume.views import ResumeListView, AddResumeView
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainMenuView.as_view()),
    path('login', MyLoginView.as_view()),
    path('signup', MySingUpView.as_view()),
    path('signup/signup/', RedirectView.as_view(url='/login')),
    path('logout', LogoutView.as_view()),
    path('vacancies/', VacancyListView.as_view()),
    path('vacancy/new', AddVacancyView.as_view()),
    path('resume/new', AddResumeView.as_view()),
    path('resumes/', ResumeListView.as_view()),
    path('home/', HomeView.as_view())
]
