# Generated by Django 2.0 on 2021-01-26 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cawa_app', '0005_auto_20210123_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='Image',
            field=models.ImageField(default='https://st3.depositphotos.com/15648834/17930/v/600/depositphotos_179308454-stock-illustration-unknown-person-silhouette-glasses-profile.jpg', upload_to='images/participant/'),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='Image',
            field=models.ImageField(default='https://st3.depositphotos.com/15648834/17930/v/600/depositphotos_179308454-stock-illustration-unknown-person-silhouette-glasses-profile.jpg', upload_to='images/researcher/'),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='Image',
            field=models.ImageField(default='https://st3.depositphotos.com/15648834/17930/v/600/depositphotos_179308454-stock-illustration-unknown-person-silhouette-glasses-profile.jpg', upload_to='images/reviewer/'),
        ),
    ]
