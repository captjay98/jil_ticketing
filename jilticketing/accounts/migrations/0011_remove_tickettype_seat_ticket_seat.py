# Generated by Django 4.1.3 on 2022-11-23 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0010_alter_ticket_expires_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tickettype",
            name="seat",
        ),
        migrations.AddField(
            model_name="ticket",
            name="seat",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
