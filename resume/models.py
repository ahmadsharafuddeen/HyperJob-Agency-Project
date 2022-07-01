from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Resume(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)







# applicant_1 = User.objects.create(username="dawood", password="ahmad2022")
# applicant_2 = User.objects.create(username="yusuf", password="muh2004")
#
# Resume.objects.create(description="Senior Backend Engineer", author=applicant_1)
# Resume.objects.create(description="Front End", author=applicant_2),
