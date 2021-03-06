# Generated by Django 2.2 on 2021-02-05 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cawa_app', '0022_auto_20210204_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Topic', models.CharField(max_length=50)),
                ('Sub_Topic', models.CharField(max_length=50)),
                ('Speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cawa_app.Researcher')),
            ],
        ),
    ]
