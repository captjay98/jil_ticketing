# Generated by Django 4.1.3 on 2022-11-21 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_alter_booking_id_alter_departure_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="ticket_type_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="accounts.tickettype"
            ),
        ),
    ]
