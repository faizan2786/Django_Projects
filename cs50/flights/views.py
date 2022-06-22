from urllib.parse import non_hierarchical
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'flights/index.html', {
        'flights': Flight.objects.all()
    })

def flight(request, flight_id):
    
    flight = Flight.objects.get(pk = flight_id)  # get the flight object from input flight id
    passengers  = flight.passengers.all() # get all passengers for given flight 
                                          #(here, .passengers method is available bacause of the related_name field we added in the Passenger model) 

    non_passangers = Passenger.objects.exclude(flight=flight) # list of passengers that are not part of the 'flight' 

    return render(request, 'flights/flight.html', {
        'flight': flight,
        'passengers': passengers,
        'non_passengers': non_passangers
        })

def book(request, flight_id):
    if request.method == 'POST':
        flight = Flight.objects.get(pk = flight_id) # get the flight object
        p_id = int(request.POST["passenger"]) # get the value of "passenger" input from the posted form (which is passenger's id)
        passenger = Passenger.objects.get(pk=p_id) # get the passenger object
        passenger.flight.add(flight) # add flight to the passenger's flight list

        return HttpResponseRedirect( reverse('flights:flight', args =(flight_id,)) ) # redirect to the flight page
    

