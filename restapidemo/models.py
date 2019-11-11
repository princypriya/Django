from django.db import models

# Create your models here.

class Employees(models.Model):
    employeename = models.CharField(max_length=100)
    empphone = models.CharField(max_length=12)
    salarly = models.IntegerField()
