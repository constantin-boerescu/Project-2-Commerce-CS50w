# Generated by Django 4.2.4 on 2023-08-15 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_remove_bids_bid_bids_amout_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bids',
            old_name='amout',
            new_name='amount',
        ),
    ]