from django.contrib import admin

# Register your models here.

from .models import Flights, Airports

admin.site.register(Flights)
admin.site.register(Airports)