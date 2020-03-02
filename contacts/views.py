from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.


def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # CHECK if enquiry has already been made
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, "Request Has Already Been Made By you for this listing")
                return redirect('/listings/'+listing_id)
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                          phone=phone, message=message, user_id=user_id)
        contact.save()

        send_mail(
            'Property Listing Enquiry',
            'There has been an inquiry made by you for ' +
            listing + ". Sign into dashboard for more info",
            'siddharthasaxena.1998@gmail.com',
            [realtor_email, 'sidsah30@gmail.com'],
            fail_silently=False
        )
        messages.success(
            request, "Request Submitted Successfully.Someone will get back to you soon.")
        return redirect('/listings/'+listing_id)
