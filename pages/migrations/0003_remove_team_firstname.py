# Generated by Django 3.1.3 on 2020-11-26 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20201126_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='firstname',
        ),
    ]
