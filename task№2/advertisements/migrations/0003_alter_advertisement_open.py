# Generated by Django 4.1.7 on 2023-02-16 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_advertisement_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='open',
            field=models.BooleanField(default=False),
        ),
    ]
