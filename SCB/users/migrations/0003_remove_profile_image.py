# Generated by Django 3.1.2 on 2020-10-02 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_year_in_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
