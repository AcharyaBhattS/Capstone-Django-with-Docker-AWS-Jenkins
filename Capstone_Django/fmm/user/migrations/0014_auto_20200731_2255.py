# Generated by Django 3.0.3 on 2020-07-31 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20200731_2252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermentoraccount',
            options={'ordering': ('-top', 'created_at')},
        ),
    ]
