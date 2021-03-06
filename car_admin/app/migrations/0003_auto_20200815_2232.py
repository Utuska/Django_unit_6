# Generated by Django 2.2.13 on 2020-08-15 19:32

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_review_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['id'], 'verbose_name': 'машина', 'verbose_name_plural': 'машины'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['id'], 'verbose_name': 'обзор', 'verbose_name_plural': 'обзоры'},
        ),
        migrations.AddField(
            model_name='car',
            name='mentions',
            field=models.IntegerField(default=app.models.Car.review_count),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=50, verbose_name='бренд'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=50, verbose_name='модель'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=100, verbose_name='описание'),
        ),
    ]
