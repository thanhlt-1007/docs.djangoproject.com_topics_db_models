# Generated by Django 5.1.4 on 2024-12-17 04:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_runner"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fruit",
            fields=[
                (
                    "name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
            ],
        ),
    ]
