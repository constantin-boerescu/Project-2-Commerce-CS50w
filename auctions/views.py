from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, AuctionListing, Bids, Comments
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

            # get the owner username
            curent_user = request.user
            new_bid = Bids.objects.create(user=curent_user, amount=price)

            # default image
            if img_url == '':
                img_url = "https://i.stack.imgur.com/mwFzF.png"
            # create a new listing
            new_listing = AuctionListing(
            owner=curent_user,
            title=title,
            description=description,
            image_url=img_url,
            price = new_bid,
            )
            # saves the data into the database

            new_listing.save()
            
            return HttpResponseRedirect(reverse("active_listings"))
        else:
            form = CreateForm()
            return render(request, "auctions/thanks.html",{
                    "title":title,
                    "description":description,
                    "img_url":img_url,
                })
        


def active_listings(request):
    '''Rendes the active listing pages'''

    # gets all of the listings
    entries = AuctionListing.objects.all()
    # renders the page
    return render(request, "auctions/active_listings.html",{
        "entries":entries
        })


def listing_page(request, listing_id):
    '''Returns the listing page by id'''

    #  gets the model by id
    listing = AuctionListing.objects.get(pk=listing_id)
    # gets the current user 
    current_user = request.user

    #get the current bid
    current_bid = listing.price

    # if the user is in the watch or not the is_in_watchlist is updated
    if current_user in listing.watch_list.all():
        is_in_watchlist = True
    else :
        is_in_watchlist = False

    comments = listing.comment

    # renders the listing page
    return render(request, "auctions/listing_page.html",{
        "listing":listing,
        "is_in_watchlist":is_in_watchlist,
        "bid":current_bid.amount,
        "comments" : comments,

        })



def add_to_watchlist(request, listing_id):
    '''Ads a user to the watchlist'''

    #  gets the lisitng model by id
    listing = AuctionListing.objects.get(pk=listing_id)
    current_user = request.user
    # gets the current user 
    listing.watch_list.add(current_user)
    # redirects to the lising page
    return HttpResponseRedirect(reverse("listing_page", args=(listing_id,)))

def remove_from_watchlist(request, listing_id):
    '''Removes a user from the watchlist'''

    #  gets the lisitng model by id
    listing = AuctionListing.objects.get(pk=listing_id)
    # gets the current user 
    current_user = request.user
    listing.watch_list.remove(current_user)
    # redirects to the lising page
    return HttpResponseRedirect(reverse("listing_page", args=(listing_id,)))

def update_bids(request, listing_id):
    '''Updates the bid amount for a listing'''
    new_bid = request.POST["new_bid"]
    # gets the lisitng model by id
    listing = AuctionListing.objects.get(pk=listing_id)
    current_user = request.user
    if int(new_bid) > int(listing.price.amount):
        update_bid = Bids(user=current_user, amount = new_bid)
        update_bid.save()
        listing.price = update_bid
        listing.save()

    return HttpResponseRedirect(reverse("listing_page", args=(listing_id,)))


'''TODO COMMENT'''
def add_comment(request, listing_id):
    current_user = request.user
    comment = request.POST["comment"]
    comment = Comments(comment = comment, user = current_user)
    print(comment.user)
    return HttpResponseRedirect(reverse("listing_page", args=(listing_id,)))