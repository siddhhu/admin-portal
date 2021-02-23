# Generated by Django 3.1.5 on 2021-01-17 13:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_auto_20210117_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 17, 19, 28, 28, 188196)),
        ),
        migrations.AlterField(
            model_name='branch',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 17, 19, 28, 28, 180220)),
        ),
        migrations.AlterField(
            model_name='college',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 17, 19, 28, 28, 179221)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 17, 19, 28, 28, 184207)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='proctor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.proctor'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='semester_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.semester'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='subject_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.subject'),
        ),
        migrations.AlterField(
            model_name='proctor',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 17, 19, 28, 28, 182213)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='branch_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.branch'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 17, 19, 28, 28, 186203)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='subject_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.subject'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 17, 19, 28, 28, 182213)),
        ),
        migrations.AlterField(
            model_name='students',
            name='branch_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.branch'),
        ),
        migrations.AlterField(
            model_name='students',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 17, 19, 28, 28, 183209)),
        ),
        migrations.AlterField(
            model_name='students',
            name='semester_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.semester'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='branch_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.branch'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='doc',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 17, 19, 28, 28, 181215)),
        ),
    ]