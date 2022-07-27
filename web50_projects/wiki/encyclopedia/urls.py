from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_name>/",views.wiki, name="wiki"),
    path("search/", views.search, name='search'),
    path("random/", views.show_random, name='random')
]
