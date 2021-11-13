# Generated by Django 3.2.8 on 2021-10-27 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobadds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobadd',
            name='hamount',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)]),
        ),
    ]
