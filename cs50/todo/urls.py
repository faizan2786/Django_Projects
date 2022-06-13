import imp
from django.urls import path
from . import views


app_name = "todo"  # define namespace for Django to find urls in this app

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
]