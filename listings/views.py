from django.shortcuts import render

# Create your views here.

# Display All the Listings


def index(request):
    return render(request, 'listings/listings.html')

# Display one particular listing


def listing(request):
    return render(request, 'listings/listing.html')

# Search Listings


def search(request):
    return render(request, 'listings/search.html')
