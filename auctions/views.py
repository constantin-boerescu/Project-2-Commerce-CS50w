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

        if form.is_valid():
            title=form.cleaned_data["title"]
            description=form.cleaned_data["description"]
            img_url=form.cleaned_data["img_url"]
            price=form.cleaned_data["price"]
            starting_bid=form.cleaned_data["start_bid"]
            auctions = AuctionListing(
            owner=request.user,
            title=title,
            description=description,
            image_url=img_url,
            price=price,
            starting_bid=starting_bid)
            auctions.save()
            print(f"{title} {description} {img_url}")
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
    