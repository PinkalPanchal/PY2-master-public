# Generated by Django 2.0 on 2021-02-27 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cawa_app', '0046_researcher_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researcher_registration',
            name='Participant_users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cawa_app.Researcher'),
        ),
    ]
