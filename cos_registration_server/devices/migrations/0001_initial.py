# Generated by Django 4.2.11 on 2024-03-15 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("applications", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Device",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uid", models.CharField(max_length=200, unique=True)),
                (
                    "creation_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="creation date"
                    ),
                ),
                (
                    "address",
                    models.GenericIPAddressField(verbose_name="device IP"),
                ),
                (
                    "grafana_dashboards",
                    models.ManyToManyField(
                        related_name="devices",
                        to="applications.grafanadashboard",
                    ),
                ),
            ],
        ),
    ]
