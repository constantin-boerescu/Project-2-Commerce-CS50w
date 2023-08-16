from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    category_title = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.category_title}"
    
class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Comments(models.Model):
    comment = models.CharField(max_length=640)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} said: {self.comment}"

class AuctionListing(models.Model):
    title = models.CharField(max_length=64)
    price = models.ForeignKey(Bids, on_delete=models.CASCADE, related_name="bid_ammount")
    description = models.CharField(max_length=640)
    image_url = models.CharField(max_length=2048, blank=True, default="https://i.stack.imgur.com/mwFzF.png")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    watch_list = models.ManyToManyField(User, blank=True, related_name="watch_list")

    def __str__(self):
        return f"{self.title} owned by: {self.owner}"



class Comments(models.Model):
    comment = models.CharField(max_length=640)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, blank=True, null=True, related_name="lisitng_commnet")
    def __str__(self):
        return f"{self.user} said: {self.comment}"