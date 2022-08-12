# Generated by Django 4.0.6 on 2022-08-12 06:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_userreservation_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreservation',
            name='email',
            field=models.EmailField(max_length=50, validators=[django.core.validators.RegexValidator(message='Check your email or put another', regex='(^[A-Za-z0-9]+[\\w_]+.[\\w_]+@[0-9A-Za-z]+\\.[a-z]{2,7}$)')]),
        ),
    ]