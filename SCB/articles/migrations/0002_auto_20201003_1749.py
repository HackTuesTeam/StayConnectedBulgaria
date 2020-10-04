# Generated by Django 3.1.2 on 2020-10-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='main_city',
        ),
        migrations.AddField(
            model_name='article',
            name='city',
            field=models.CharField(choices=[('SOFIA', 'Sofia'), ('BURGAS', 'Burgas'), ('PLOVDIV', 'Plovdiv'), ('VARNA', 'Varna'), ('RUSE', 'Ruse')], default='SOFIA', max_length=10),
        ),
    ]