from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, 'users/index.html')

def login_view(request):
    if request.method == 'POST':
        # get the username and password from posted form
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password) # authenticate the user

        # if user is authenticated successfully
        if user is not None:
            login(request,user) # login the user
            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request, 'users/login.html', {'message': 'username or password incorrect!'})
    
    # render login page for get request
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request) # logout the session
    return render(request, 'users/login.html', {'message': 'Logged Out!'})


