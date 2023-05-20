# Generated by Django 3.0.3 on 2020-07-30 20:21

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0011_auto_20200721_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='INR', max_digits=10),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='INR', max_digits=10),
        ),
    ]
