# Generated by Django 3.1.5 on 2021-01-14 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20210114_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 37, 38, 575240)),
        ),
        migrations.AlterField(
            model_name='branch',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 37, 38, 565267)),
        ),
        migrations.AlterField(
            model_name='college',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 37, 38, 563273)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 37, 38, 572248)),
        ),
        migrations.AlterField(
            model_name='proctor',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 37, 38, 568260)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='answer',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='questions',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 37, 38, 574242)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option_a',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option_b',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option_c',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option_d',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='semester',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 37, 38, 567261)),
        ),
        migrations.AlterField(
            model_name='students',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 37, 38, 570253)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 37, 38, 566264)),
        ),
    ]
