# Generated by Django 4.1.3 on 2022-12-03 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0012_trip_arrival_time_trip_departure_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="tickettype",
            name="seats",
            field=models.IntegerField(default=20),
        ),
    ]