# Generated by Django 4.2.1 on 2023-11-13 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='burger',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
