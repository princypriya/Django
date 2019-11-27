
from django.shortcuts import render
from django.http import HttpResponse

from .models import Employees


def regn(request):
    return render(request, 'register.html')

def addnewrec(request):
    a = request.GET["empid"]
    b = request.GET["empname"]
    c = request.GET["age"]
    e = Employees(empid = a, empname = b, age = c)
    e.save()
    return render(request, 'emprecords.html', { 'records' : e }) 
