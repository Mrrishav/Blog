# Generated by Django 3.1.8 on 2022-02-21 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_auto_20220221_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amtfer',
            old_name='balance',
            new_name='bal',
        ),
        migrations.RenameField(
            model_name='amtfer',
            old_name='uname',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='amtdep',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 21, 13, 15, 42, 79247)),
        ),
    ]
