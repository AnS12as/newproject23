# Generated by Django 5.0.7 on 2024-07-17 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="preview",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="preview",
            field=models.URLField(blank=True, null=True),
        ),
    ]
