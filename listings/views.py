from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . choices import district_choices, room_choices, rooms_choices

# Create your views here.

def listings(request):
    listings = Listing.objects.order_by('list_date').filter(is_published=True)
    paginator = Paginator(listings,3)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context = {"listings":paged_listings}
    return render(request, 'listings/listings.html',context)

def listing(request,listing_id):
    listing = Listing.objects.get(id=listing_id)
    context = {"listing" : listing}
    return render(request, 'listings/listing.html',context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            queryset_list = queryset_list.filter(district__iexact=district)
    if 'rooms' in request.GET:
        rooms = request.GET['rooms']
        if rooms:
            queryset_list = queryset_list.filter(rooms__lte=rooms)
    if 'room_type' in request.GET:
        room_type = request.GET['room_type']
        if room_type:
            queryset_list = queryset_list.filter(room_type__iexact=room_type)
    context = {"listings" : queryset_list,
               "district_choices" : district_choices,
               "room_choices" : room_choices,
               "rooms_choices" : rooms_choices,
               "values" : request.GET

    }
    return render(request, 'listings/search.html', context )