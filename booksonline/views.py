from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import  HttpResponseRedirect
from .models import books



def book(request):
    e = books.objects.all()
    #e=books.objects.filter(price<=400)
    return render(request, 'books.html',{"books":e})

def filtering(request):
    cost = request.GET["price"]
    e = books.objects.all()
    ee  = e.filter(price__lte=cost)
    return render(request, 'books.html',{"books":ee})


def booksrch(request):
    bid = request.GET["bookid"]
    ee = books.objects.all()
    book = get_object_or_404(ee, id=bid)
    return render(request, 'results.html', {'book': book})
    

    



    # https://data-flair.training/blogs/django-crud-example/

