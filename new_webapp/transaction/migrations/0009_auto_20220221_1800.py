# Generated by Django 3.1.8 on 2022-02-21 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0008_auto_20220221_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='amtfer',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 21, 18, 0, 15, 857339)),
        ),
        migrations.AlterField(
            model_name='amtdep',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 21, 18, 0, 15, 810966)),
        ),
    ]
