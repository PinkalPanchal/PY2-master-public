# Generated by Django 3.1.7 on 2021-04-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cawa_app', '0086_auto_20210409_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcher_registration',
            name='Breakfast_Coupon',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='researcher_registration',
            name='Lunch_Coupon',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='researcher_registration',
            name='Tea_Coupon',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
