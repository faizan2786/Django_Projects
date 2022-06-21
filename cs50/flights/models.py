from django.db import models

# Create your models here.

class Airports(models.Model):
    city = models.CharField(max_length=20)
    code = models.CharField(max_length=3)

    def __str__(self) -> str:
        return f"{self.city} ({self.code})"

class Flights(models.Model):
    origin = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="departures")   # related name is the key name that we can use to get the reverse relation 
                                                                                                # (all origin cities of specific airport - all outgoing flights from the airport)
    destination = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="arrivals") # (related_name -> key to get all incoming flights to an airport) 
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}. {self.origin} to {self.destination}"