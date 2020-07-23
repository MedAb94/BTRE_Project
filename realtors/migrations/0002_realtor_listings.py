# Generated by Django 3.0.4 on 2020-04-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_remove_listing_realtor'),
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='listings',
            field=models.ManyToManyField(to='listings.Listing'),
        ),
    ]
