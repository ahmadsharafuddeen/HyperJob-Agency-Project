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
from django.views.generic import RedirectView
from vacancy.views import MainPageView, VacancyListView,\
    ProfilePageView, VacancyFormView
from resume.views import ResumeListView, SignupView, \
    SignInView, LogoutView, ResumeFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", MainPageView.as_view()),
    path("vacancies", VacancyListView.as_view()),
    path("resumes", ResumeListView.as_view()),
    path('signup', SignupView.as_view()),
    path('login', SignInView.as_view()),
    path('logout', LogoutView.as_view()),
    path('resume/new', ResumeFormView.as_view()),
    path('vacancy/new', VacancyFormView.as_view()),
    path('home', ProfilePageView.as_view()),

    # some other patterns
    path('login/', RedirectView.as_view(url='/login')),
    path('logout/', RedirectView.as_view(url='/logout')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path("vacancies/", RedirectView.as_view(url='/vacancies')),
    path("resumes/", RedirectView.as_view(url='/resumes')),
    path("home/", RedirectView.as_view(url='/home')),
    # path("resume/new/", RedirectView.as_view(url='/resume/new'))
]
