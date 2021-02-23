# Generated by Django 3.1.5 on 2021-01-08 10:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='college_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.college'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='college_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.college'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 57, 19, 460104)),
        ),
        migrations.AlterField(
            model_name='branch',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 57, 19, 450132)),
        ),
        migrations.AlterField(
            model_name='college',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 57, 19, 449133)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 57, 19, 458109)),
        ),
        migrations.AlterField(
            model_name='proctor',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 57, 19, 453123)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 57, 19, 459107)),
        ),
        migrations.AlterField(
            model_name='students',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 57, 19, 454120)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 57, 19, 451129)),
        ),
    ]
