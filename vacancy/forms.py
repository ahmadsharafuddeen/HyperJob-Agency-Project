from .models import Vacancy
from django.forms import ModelForm
from django.http import HttpResponseForbidden


class VacancyForm(ModelForm):
    def __int__(self, *args, **kwargs):
        user = kwargs.pop('user', None)

        if user is not None and not user.is_staff:
            return HttpResponseForbidden

    class Meta:
        model = Vacancy
        fields = ['description']