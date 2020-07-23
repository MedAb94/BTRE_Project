from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .choices import *
from .models import Listing


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    paged = paginator.get_page(request.GET.get('page'))
    context = {
        'listings': paged
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listings = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listings
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__iexact=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__iexact=city)
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            listings = listings.filter(city__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(city__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET.get('price')
        if price:
            listings = listings.filter(price__lte=price)

    con = {
        'bedrooms': bedrooms_choices,
        'prices': prices_choices,
        'states': states_choices,
        'listings': listings,
        'values': request.GET,

    }
    return render(request, 'listings/search.html', con)
