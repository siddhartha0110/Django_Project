from django.shortcuts import render


# Display All the Listings
def index(request):
    return render(request, 'listings/listings.html')


# Display one particular listing
def listing(request):
    return render(request, 'listings/listing.html')


# Search Listings
def search(request):
    return render(request, 'listings/search.html')
