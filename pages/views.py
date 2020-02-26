from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing

# Create your views here.


def index(request):
    listing = Listing.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listing
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
