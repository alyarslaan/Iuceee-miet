# Generated by Django 3.2.5 on 2021-08-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MOM',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('task', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]