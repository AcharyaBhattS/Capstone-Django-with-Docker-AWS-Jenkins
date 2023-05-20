# Generated by Django 3.0.3 on 2020-05-27 15:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_usermentorschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usereducation',
            name='school_start',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1920)]),
        ),
    ]
