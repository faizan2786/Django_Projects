from django.shortcuts import render
from datetime import datetime;

# Create your views here.
def newyear(request):
    today = datetime.now()
    context = {"newyear": today.month==1 and today.date==1}
    return render(request, "newyear.html", context)