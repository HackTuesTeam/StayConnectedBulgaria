# Generated by Django 3.1.2 on 2020-10-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201003_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='content',
            field=models.TextField(default='just user'),
        ),
    ]
