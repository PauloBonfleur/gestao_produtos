# Generated by Django 2.2.3 on 2019-07-23 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='Data',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
