# Generated by Django 2.2 on 2021-03-02 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cawa_app', '0047_auto_20210227_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='researcher_registration',
            old_name='Participant_users',
            new_name='Researcher_users',
        ),
    ]
