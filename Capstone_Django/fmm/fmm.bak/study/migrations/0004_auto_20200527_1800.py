# Generated by Django 3.0.3 on 2020-05-27 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200527_1800'),
        ('study', '0003_workshoprecording'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='mentor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='user.UserMentorAccount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workshop',
            name='mentor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='workshops', to='user.UserMentorAccount'),
            preserve_default=False,
        ),
    ]