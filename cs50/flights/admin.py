from ast import Pass
from django.contrib import admin

from .models import Flight, Airport, Passenger

# create customise display for flight model (in admin interface)

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ('flight', )  # using horizontal filter view on 'flight' (many-to-many) field
                                    # (to have side by side list of selected and unselected flights for each passenger)


# Register your models here.

admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passenger, PassengerAdmin)  