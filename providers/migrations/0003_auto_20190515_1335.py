# Generated by Django 2.2.1 on 2019-05-15 11:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_auto_20190515_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='phone_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Please, enter the phone number in a correct format.', regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
