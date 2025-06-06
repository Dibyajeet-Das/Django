from django.shortcuts import render
from django.http import HttpResponse
#Importing the destination from models
from . models import Destination

# Create your views here.

def index(request):
    # Passing the Objects here for dynamic content 
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = "The City that never sleeps"
    dest1.img = 'destination_1.jpg'
    dest1.price = 1000
    dest1.offer = False 
    
    dest2 = Destination()
    dest2.name = 'Shanghai'
    dest2.desc = "one of the most populous cities in the world and a global financial center"
    dest2.img = 'destination_2.jpg'
    dest2.price = 900
    dest2.offer = True 
      
    dest3 = Destination()
    dest3.name = 'Moscow'
    dest3.desc = "city that never rests"
    dest3.img = 'destination_3.jpg'
    dest3.price = 1400
    dest3.offer = False      
    
    dests = [dest1, dest2, dest3]
    
    return render(request, "index.html", {'dests': dests})
#1.51



