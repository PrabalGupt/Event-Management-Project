# Generated by Django 4.2.2 on 2023-08-04 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventdetails',
            name='image',
        ),
        migrations.RemoveField(
            model_name='eventdetails',
            name='user_id',
        ),
    ]
