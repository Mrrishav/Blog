# Generated by Django 3.1.8 on 2022-02-21 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_auto_20220221_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amtdep',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 21, 12, 52, 46, 954297)),
        ),
    ]
