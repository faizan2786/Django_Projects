# url config for firstapp
from django.urls import path
from . import views

# configure list of urls (paths) available from current app to the corresponding views
urlpatterns = [
    path('', views.index, name="index"), # default path for the app
    path("faizan/", views.faizan, name="faizan"),
    #path("<str:myname>/", views.greet, name="greet"),
    # the url string (str) will be given as argument 'name' to the views.greet function
    path('aboutme/',views.aboutme, name="myinfo"),
    path('myinfo/', views.aboutme, name="myinfo"),
    path("<str:name>/", views.hello, name="hello"),
]
