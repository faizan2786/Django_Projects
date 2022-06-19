import email
from django.db import models

# Create your models here

# a toy User table example to test django models
class Users(models.Model):
    name = models.CharField(max_length=128)   # create 'name' field
    email = models.CharField(max_length=128)  # creat 'email' field

# an Items table to represent task items 
class Items(models.Model):
    name=models.CharField(max_length=128) 
    date=models.DateField(auto_now_add=True) # automatically add date only when the object is created
    status=models.SmallIntegerField(default=0) # 0 = notstarted (default valueq§), 1 = started, 2 = finished
