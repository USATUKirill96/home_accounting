# Generated by Django 3.0.5 on 2020-04-28 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapi', '0006_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='источник дохода'),
        ),
        migrations.AlterField(
            model_name='spending',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='наименование траты'),
        ),
    ]