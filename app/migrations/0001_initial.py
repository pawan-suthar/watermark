# Generated by Django 4.1.3 on 2023-01-03 10:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ImageModel",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("image", models.ImageField(upload_to="images")),
                ("water_mark", models.CharField(max_length=100)),
            ],
        ),
    ]
