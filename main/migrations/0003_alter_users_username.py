# Generated by Django 5.1.6 on 2025-03-02 23:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_alter_ertaklar_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="username",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
