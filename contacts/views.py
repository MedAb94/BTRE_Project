from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Contact


# Create your views here.

def index(request):
    if request.method == 'POST':
        listing = request.POST.get('listing')
        listing_id = request.POST.get('listing_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id')
        realtor_email = request.POST.get('realtor_email')
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                          phone=phone, message=message, user_id=user_id)
        contact.save()
        messages.success(request, "Query submitted successufly")
        return redirect('/listings/'+user_id)
    return render(request, 'index')