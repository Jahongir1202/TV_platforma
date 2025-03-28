# Generated by Django 5.1.6 on 2025-03-02 22:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ertaklar",
            options={"ordering": ["order"]},
        ),
        migrations.RenameField(
            model_name="ertaklar",
            old_name="youtube_url",
            new_name="video_url",
        ),
        migrations.AlterField(
            model_name="ertaklar",
            name="order",
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]
