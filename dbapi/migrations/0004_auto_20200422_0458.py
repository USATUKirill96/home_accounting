# Generated by Django 3.0.5 on 2020-04-22 04:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapi', '0003_auto_20200422_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spending',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='дата'),
        ),
    ]
