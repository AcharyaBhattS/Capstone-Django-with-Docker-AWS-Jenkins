# Generated by Django 3.0.3 on 2020-05-29 13:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0006_auto_20200528_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studypayment',
            name='user',
        ),
        migrations.AddField(
            model_name='studypayment',
            name='appointment_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='study.AppointmentUser'),
        ),
        migrations.AddField(
            model_name='studypayment',
            name='workshop_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='study.WorkshopUser'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='amount',
            field=models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(50)]),
        ),
    ]
