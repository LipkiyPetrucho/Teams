# Generated by Django 5.1 on 2024-08-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="city",
            field=models.CharField(default="Самара", max_length=100),
        ),
    ]
