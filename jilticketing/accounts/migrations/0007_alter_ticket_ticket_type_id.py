# Generated by Django 4.1.3 on 2022-11-21 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_alter_ticket_ticket_type_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="ticket_type_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="ticket_types",
                to="accounts.tickettype",
            ),
        ),
    ]
