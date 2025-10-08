from django.shortcuts import render
from listings.models import Listing
# Create your views here.

def index(request):
    print(request)
    print(request.path)
    listings = Listing.objects.filter(is_published=True)[:3]
    context = {'listings': listings}
    return render(request,'pages/index.html',context)

def about(request):
    print(request.path)
    return render(request,'pages/about.html')