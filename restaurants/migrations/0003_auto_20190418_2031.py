# Generated by Django 2.0.6 on 2019-04-18 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurant',
            new_name='RestaurantLocation',
        ),
    ]
