from django.shortcuts import render
from listings.models import Listing
# Create your views here.

from doctors.models import Doctor
from listings.choices import district_choices, room_choices, rooms_choices

def index(request):

    listings = Listing.objects.filter(is_published=True)[:3]
    context = {'listings': listings,
               "district_choices": district_choices,
               'room_choices' : room_choices,
               'rooms_choices' : rooms_choices
               }
    return render(request,'pages/index.html',context)

def about(request):
    print(request.path)
    return render(request,'pages/about.html')

