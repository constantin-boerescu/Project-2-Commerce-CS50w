# Generated by Django 4.2.4 on 2023-08-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_remove_auctionlisting_comment_comments_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
