# Generated by Django 3.1.5 on 2021-01-14 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20210114_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 5, 57, 979116)),
        ),
        migrations.AlterField(
            model_name='branch',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 5, 57, 968145)),
        ),
        migrations.AlterField(
            model_name='college',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 5, 57, 967147)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 5, 57, 976124)),
        ),
        migrations.AlterField(
            model_name='proctor',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 5, 57, 972134)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 5, 57, 978123)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='questions',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='semester',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 5, 57, 971138)),
        ),
        migrations.AlterField(
            model_name='students',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 5, 57, 973132)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 5, 57, 970141)),
        ),
    ]