import imp
from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here

# define an html form using django forms
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")  # creates a character (text) input field and does client side validation
    priority = forms.IntegerField(label = "Priority", min_value=1) # creates a numeric input field and does client side validation

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []     # create an empty list of new tasks for current session

    return render(request,"index.html", {"tasks":  request.session["tasks"]})

def add(request):

    # if the request is of type 'POST' (when user submits a new task)
    if request.method == "POST":
        form = NewTaskForm(request.POST) # populate the form with user submitted data
        if form.is_valid():
            task = form.cleaned_data["task"]  # get the variable 'task'(defined in the NewTaskForm object) from the form's user data 
            
            request.session["tasks"] += [task]  # update list of tasks for current session

            return HttpResponseRedirect(reverse("todo:index"))  # Redirect user to list of tasks- 
                                                                # reverse("todo:index") -> resolve url for name 'index' in 'todo' app
        else:
            context = {"form": form}  # 'form' is an existing form with user data filled in
            return render(request, "add.html", context)  # display the existing form if not valid
    
    else: # render a new form for GET method
        context = {"form": NewTaskForm()}  # generate new form and pass it to the add.html page
        return render(request, "add.html", context)