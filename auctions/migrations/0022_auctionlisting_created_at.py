# Generated by Django 4.2.4 on 2023-08-19 09:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_comments_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
