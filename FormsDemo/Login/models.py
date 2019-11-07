from django.db import models

# Create your models here.

class LoginForm(models.Model):
    userid = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    desc = models.TextField()
    bill = models.CharField(max_length = 50)
    pincode = models.CharField(max_length = 50)

class Todo(models.Model):
    added_date = models.DateTimeField()
    text  = models.CharField(max_length=200)
    
