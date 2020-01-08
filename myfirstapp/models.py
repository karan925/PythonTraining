from django.db import models


# Create your models here.


class Portfolio(models.Model):
    name = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=5, unique=False)
    age = models.DateField()
    address = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    assignee_name = models.ForeignKey('Portfolio', on_delete=models.PROTECT)
    item_name = models.CharField(max_length=50, unique=True)
    assigned_date = models.DateTimeField()
    return_date = models.DateTimeField()

    def __str__(self):
        return self.item_name


class Session(models.Model):
    name = models.ForeignKey('Portfolio', on_delete=models.CASCADE)
    store_name = models.CharField(max_length=50, unique=True)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField()

    def __str__(self):
        return self.store_name
