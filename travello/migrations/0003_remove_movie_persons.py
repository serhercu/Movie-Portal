# Generated by Django 3.2 on 2021-05-22 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_auto_20210522_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='persons',
        ),
    ]
