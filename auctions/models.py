from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category_title = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.category_title}"


class AuctionListing(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=640)
    image_url = models.CharField(max_length=2048)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} owned by: {self.owner}"

class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amout = models.DecimalField(max_digits=10, decimal_places=2)
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amout} paid by {self.user} for {self.listing}"


class Comments(models.Model):
    comment = models.CharField(max_length=640)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} said: {self.comment}"