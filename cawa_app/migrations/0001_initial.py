# Generated by Django 2.0 on 2021-01-18 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mphone', models.IntegerField()),
                ('mimage', models.ImageField(default='', upload_to='images/participant/')),
                ('mtype', models.CharField(default='student', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mphone', models.IntegerField()),
                ('mimage', models.ImageField(default='', upload_to='images/researcher/')),
                ('mspecial', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mphone', models.IntegerField()),
                ('mimage', models.ImageField(default='', upload_to='images/reviewer/')),
                ('mspecial', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('musertype', models.CharField(default='participant', max_length=20)),
                ('mfname', models.CharField(max_length=50)),
                ('mlname', models.CharField(max_length=50)),
                ('memail', models.EmailField(max_length=254)),
                ('mpassword', models.CharField(max_length=50)),
                ('mcpassword', models.CharField(max_length=50)),
                ('mactive', models.CharField(default='Inactive', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='reviewer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cawa_app.User'),
        ),
        migrations.AddField(
            model_name='researcher',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cawa_app.User'),
        ),
        migrations.AddField(
            model_name='participant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cawa_app.User'),
        ),
    ]
