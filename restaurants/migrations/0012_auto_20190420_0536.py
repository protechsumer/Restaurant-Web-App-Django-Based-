# Generated by Django 2.0.6 on 2019-04-20 00:06

from django.db import migrations, models
import restaurants.validators


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0011_auto_20190420_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[restaurants.validators.validate_category]),
        ),
    ]
