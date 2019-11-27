from django.db import models

# Create your models here.

class Employees(models.Model):
    empid = models.CharField(max_length=10)
    empname = models.CharField(max_length=50)
    age = models.IntegerField()

class Departments(models.Model):
    deptid = models.CharField(max_length=10)
    deptname = models.CharField(max_length=50)

class Manager(models.Model):
    manid=models.CharField(max_length=10)
    manname=models.CharField(max_length=50)