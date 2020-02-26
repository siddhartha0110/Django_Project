from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Display All the Listings
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


# Display one particular listing
def listing(request, listing_id):
    return render(request, 'listings/listing.html')


# Search Listings
def search(request):
    return render(request, 'listings/search.html')
