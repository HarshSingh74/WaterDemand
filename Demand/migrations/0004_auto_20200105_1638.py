# Generated by Django 3.0 on 2020-01-05 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Demand', '0003_auto_20200105_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eastern',
            name='normsPred',
        ),
        migrations.RemoveField(
            model_name='island',
            name='normsPred',
        ),
        migrations.RemoveField(
            model_name='western',
            name='normsPred',
        ),
    ]
