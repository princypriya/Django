from django.db import models

# Create your models here.
class Prodmaster(models.Model):
    prodname = models.CharField(max_length=100)