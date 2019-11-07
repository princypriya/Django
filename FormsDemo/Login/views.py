from django.shortcuts import render
from django.http import HttpResponse
from .models import LoginForm
from .forms import Loginscreen
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect
# Create your views here.
def showscreen(request):
    form = Loginscreen(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, 'Logindata.html', context)


def todofn(request):
    todos = Todo.objects.all().order_by("-added_date")
    return render(request, 'todo.html', { "todos": todos} )

def additem(request):
    added_date = timezone.now()
    text = request.POST["itemname"]
    Todo.objects.create(added_date = added_date, text = text)
    return HttpResponseRedirect("/todo/")

def deleteitem(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/todo/")
