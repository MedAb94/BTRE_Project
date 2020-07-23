from django.shortcuts import get_object_or_404, render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import prices_choices, states_choices, bedrooms_choices


def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    con = {
        'listings': listings,
        'bedrooms': bedrooms_choices,
        'prices': prices_choices,
        'states': states_choices,

    }
    return render(request, 'pages/index.html', con)


def about(request):
    realtors = Realtor.objects.order_by('hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp': mvp_realtors
    }
    return render(request, 'pages/about.html', context)



