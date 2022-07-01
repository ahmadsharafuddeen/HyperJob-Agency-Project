from django.shortcuts import render
from django.views import View
from .models import Vacancy
from .forms import VacancyForm
from django.views.generic.edit import FormView
from django.views.generic import ListView, CreateView
from django.http import HttpResponseForbidden


# Create your views here.
class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "vacancy/index.html")


class VacancyListView(ListView):
    queryset = Vacancy.objects.all()
    context_object_name = 'vacancies'
    template_name = "vacancy/vacancies.html"


class VacancyFormView(CreateView):
    form_class = VacancyForm
    template_name = "vacancy/create_vacancy.html"
    success_url = "/home"

    def form_valid(self, form):
        if self.request.user.is_staff:
            vacancy = form.save(commit=False)
            vacancy.author = self.request.user
            vacancy.save()
            return super().form_valid(form)
        else:
            return HttpResponseForbidden()


class ProfilePageView(CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, "vacancy/profile_page.html")

