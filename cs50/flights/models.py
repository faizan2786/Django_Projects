from django.db import models

# Create your models here.

class Airport(models.Model):
    city = models.CharField(max_length=20)
    code = models.CharField(max_length=3)

    def __str__(self) -> str:
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")   # related name is the key name that we can use to get the reverse relation 
                                                                                                # (all origin cities of specific airport - all outgoing flights from the airport)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals") # (related_name -> key to get all incoming flights to an airport) 
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}. {self.origin} to {self.destination}"

class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    flight = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"