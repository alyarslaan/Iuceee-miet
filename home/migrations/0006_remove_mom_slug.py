# Generated by Django 3.2.5 on 2021-08-09 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_mom_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mom',
            name='slug',
        ),
    ]
