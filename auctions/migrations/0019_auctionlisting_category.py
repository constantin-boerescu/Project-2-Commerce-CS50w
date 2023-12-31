# Generated by Django 4.2.4 on 2023-08-18 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_auctionlisting_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='auctions.categories'),
        ),
    ]
