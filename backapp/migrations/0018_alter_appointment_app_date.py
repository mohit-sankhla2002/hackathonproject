# Generated by Django 5.0.2 on 2024-02-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0017_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='app_date',
            field=models.DateTimeField(unique=True),
        ),
    ]