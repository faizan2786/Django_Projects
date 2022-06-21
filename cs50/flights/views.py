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

    return render(request, 'flights/flight.html', {
        'flight': flight,
        'passengers': passengers
        })
