# Generated by Django 2.0.6 on 2019-04-28 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_profile_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='activation_key',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]