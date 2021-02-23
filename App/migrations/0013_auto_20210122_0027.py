# Generated by Django 3.1.5 on 2021-01-21 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_auto_20210121_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 22, 0, 27, 43, 218735)),
        ),
        migrations.AlterField(
            model_name='branch',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 22, 0, 27, 43, 208527)),
        ),
        migrations.AlterField(
            model_name='college',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 22, 0, 27, 43, 207530)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 22, 0, 27, 43, 213716)),
        ),
        migrations.AlterField(
            model_name='proctor',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 22, 0, 27, 43, 208527)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 22, 0, 27, 43, 214715)),
        ),
        migrations.AlterField(
            model_name='semester',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 22, 0, 27, 43, 208527)),
        ),
        migrations.AlterField(
            model_name='students',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 22, 0, 27, 43, 208527)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 22, 0, 27, 43, 208527)),
        ),
    ]