# Generated by Django 4.2.4 on 2023-08-16 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_remove_auctionlisting_comment_comments_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='listing',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionlisting'),
        ),
    ]
