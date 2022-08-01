from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_name>/",views.wiki, name="wiki"),
    path("search/", views.search, name='search'),
    path("random/", views.show_random, name='random'),
    path("add/",views.add_entry, name = 'add'),
    path("edit/<str:entry_name>/", views.edit_entry, name='edit'),
    path('save/', views.save_entry, name='save'),
]
