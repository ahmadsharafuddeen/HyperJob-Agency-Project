from django.shortcuts import render
from django.views import View
from .models import Resume
from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .forms import ResumeForm
# Create your views here.


class ResumeListView(ListView):
    queryset = Resume.objects.all()
    context_object_name = "resumes"
    template_name = "resume/resumes.html"


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'resume/signup.html'


class SignInView(LoginView):
    redirect_authenticated_user = True
    template_name = 'resume/signin.html'


class ResumeFormView(CreateView):
    form_class = ResumeForm
    template_name = "resume/create_resume.html"
    success_url = "/home"
    # queryset = Resume.objects.all()

    def form_valid(self, form):
        resume = form.save(commit=False)
        resume.author = self.request.user
        resume.save()
        return super().form_valid(form)









