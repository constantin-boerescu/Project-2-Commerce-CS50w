from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("active_listings", views.active_listings, name="active_listings"),
    path("<int:listing_id>", views.listing_page, name="listing_page"),
    path("<int:listing_id>/add_to_watchlist", views.add_to_watchlist, name="add_to_watchlist"),
    path("<int:listing_id>/remove_from_watchlist", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("<int:listing_id>/update_bids", views.update_bids, name="update_bids"),
    path("<int:listing_id>/add_comment", views.add_comment, name="add_comment"),
    path("<int:listing_id>/close_listing", views.close_listing, name="close_listing"),
    path("watch_list", views.watch_list, name="watch_list"),



]
