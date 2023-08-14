from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, AuctionListing
from django.contrib.auth.decorators import login_required
from .forms import CreateForm

def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create_listing(request):
    '''Let the user to make a new listing'''
    if request.method == "GET":
        form = CreateForm()
        return render(request, "auctions/create_listing.html",{
            "form":form
        })
    
    else:

        form = CreateForm(request.POST)
        # if the data is valid get the data form
        if form.is_valid():
            title=form.cleaned_data["title"]
            description=form.cleaned_data["description"]
            img_url=form.cleaned_data["img_url"]
            price=form.cleaned_data["price"]
            starting_bid=form.cleaned_data["start_bid"]

            # get the owner username
            curent_user = request.user

            # create a new listing
            new_listing = AuctionListing(
            owner=curent_user,
            title=title,
            description=description,
            image_url=img_url,
            price=float(price),
            starting_bid=float(starting_bid))

            # saves the data into the database
            new_listing.save()
            
            return render(request, "auctions/thanks.html",{
                    "title":title,
                    "description":description,
                    "img_url":img_url,
                })
        else:
            form = CreateForm()
            return render(request, "auctions/thanks.html",{
                    "title":title,
                    "description":description,
                    "img_url":img_url,
                })
        


def active_listings(request):
    entries = AuctionListing.objects.all()
    return render(request, "auctions/active_listings.html",{
        "entries":entries
        })

'''TO BE CORRECTED'''
def listing_page(request, listing_id):
    listing = AuctionListing.objects.get(pk=listing_id)
    current_user = request.user
    print(current_user)
    is_in_wathclist = False
    print(listing.watch_list.values_list('id', flat=True))
    if current_user in listing.watch_list.values_list('id', flat=True):
        print("+++++++++++++++IT ITS+++++++++++=")
        is_in_wathclist = True

    return render(request, "auctions/listing_page.html",{
        "listing":listing,
        "is_in_wathclist":is_in_wathclist,
        })
'''TO BE CORRECTED'''

def add_to_watchlist(request, listing_id):
    listing = AuctionListing.objects.get(pk=listing_id)
    current_user = request.user
    listing.watch_list.add(current_user)
    print("ADDED")
    return HttpResponseRedirect(reverse("listing_page", args=(listing_id,)))
