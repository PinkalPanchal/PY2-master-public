# Generated by Django 2.2 on 2021-03-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cawa_app', '0053_co_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcher_registration',
            name='Members',
            field=models.CharField(default=1, max_length=10),
        ),
    ]