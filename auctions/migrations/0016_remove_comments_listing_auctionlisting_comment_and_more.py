# Generated by Django 4.2.4 on 2023-08-16 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_alter_comments_listing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='listing',
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='add_comment', to='auctions.comments'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=640),
        ),
    ]