# Generated by Django 3.2 on 2021-06-09 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djago', '0004_alter_projet_date_pub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='date_pub',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 9, 19, 29, 22, 48047), max_length=30, verbose_name='Date de Publication du Projet'),
        ),
    ]
