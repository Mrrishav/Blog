# Generated by Django 3.1.8 on 2022-02-20 08:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_auto_20220220_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='amtdep',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 20, 14, 18, 26, 771603)),
        ),
    ]