# Generated by Django 2.2.1 on 2019-05-16 19:51

from django.db import migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0005_auto_20190516_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicearea',
            name='polygon',
            field=djgeojson.fields.PointField(blank=True, default=dict),
        ),
    ]
