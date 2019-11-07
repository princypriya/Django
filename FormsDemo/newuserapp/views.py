from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def newuser_home(request):
    print("here")
    if request.method == 'POST':
        form =  UserCreationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, 'Account for user {} is created!'.format(username))
            return redirect('/gohome/' )
    else:
        form = UserCreationForm()
    return render(request, 'newuser.html', {'form':form})
