# Generated by Django 5.1.4 on 2024-12-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0014_person_birth_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("name", models.CharField(max_length=100)),
                ("tagline", models.TextField()),
            ],
        ),
    ]
