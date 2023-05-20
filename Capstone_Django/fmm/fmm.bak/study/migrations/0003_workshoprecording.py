# Generated by Django 3.0.3 on 2020-05-15 11:22

from django.db import migrations, models
import django.db.models.deletion
import fmm.study.models
import fmm.utils.storage


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_auto_20200514_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkshopRecording',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('video', models.FileField(storage=fmm.utils.storage.OverwriteStorage(), upload_to=fmm.study.models.workshop_recording_upload_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recordings', to='study.Workshop')),
            ],
            options={
                'db_table': 'workshop_recording',
                'ordering': ('id',),
            },
        ),
    ]
