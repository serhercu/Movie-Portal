# Generated by Django 3.2 on 2021-05-18 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_remove_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='travello.director', unique=True),
            preserve_default=False,
        ),
    ]