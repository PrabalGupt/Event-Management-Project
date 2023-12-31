# Generated by Django 4.2.2 on 2023-08-04 10:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('is_liked', models.BooleanField(default=False)),
                ('user_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('userName', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(8, 'the field must contain at least 8 characters')])),
            ],
        ),
    ]
