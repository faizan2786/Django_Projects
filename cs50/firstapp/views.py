from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h2 style="color:red;">Hello, World from Django app!</h2>')

def faizan(request):
    return HttpResponse('<h3 style="color:blue;">Hello, Faizan!</h3>')

def greet(request, myname): # name is the argument
    return HttpResponse(f'<h1 style="color:green;">Hello, {myname.capitalize()}!</h1>')

# render an html page (from templates folder of current app (firstapp))
def aboutme(request):
    return render(request, "myinfo/index.html")  

# render an html page - using python variable!
def hello(request, name):
    context = {"name": name.capitalize()} # context is the dictionary of variables which can be passed to django templates i.e. 'hello.html' here
    return render(request, "hello.html", context) 
    