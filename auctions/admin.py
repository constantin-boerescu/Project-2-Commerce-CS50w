from django.contrib import admin
from .models import User, AuctionListing, Comments, Categories
# Register your models here.
admin.site.register(User)
admin.site.register(AuctionListing)
admin.site.register(Comments)
admin.site.register(Categories) 