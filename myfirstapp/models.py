from django.db import models

# Create your models here.


class Portfolio(models.Model):
    name = models.CharField(max_length=10, unique=False)
    gender = models.CharField(max_length=5, unique=False)
    age = models.DateField()
    address = models.CharField(max_length=50, unique=False)
