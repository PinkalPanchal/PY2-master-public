# Generated by Django 2.0 on 2021-01-27 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cawa_app', '0012_auto_20210127_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='Image',
            field=models.ImageField(default='avatar-01.jpg', upload_to='images/participant/'),
        ),
    ]
