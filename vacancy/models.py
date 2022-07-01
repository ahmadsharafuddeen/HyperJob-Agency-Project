from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Vacancy(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)



# posted_by_1 = User.objects.create(username="muhammad", password="muhammad@gmail.com")
# posted_by_2 = User.objects.create(username="adam", password="adam@gmail.com")

# Vacancy.objects.create(description="Senior Backend Engineer", author=posted_by_1)
# Vacancy.objects.create(description="Product Manager", author=posted_by_2)
