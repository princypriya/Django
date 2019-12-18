from django.db import models
class books(models.Model):
    bookid=models.CharField(max_length=10)
    bookname=models.CharField(max_length=50)
    price = models.IntegerField()



