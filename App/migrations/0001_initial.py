# Generated by Django 3.1.5 on 2021-01-08 09:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(max_length=100)),
                ('doc', models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 23, 38, 500972))),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('college_id', models.AutoField(primary_key=True, serialize=False)),
                ('college_name', models.CharField(max_length=200)),
                ('college_code', models.CharField(max_length=200)),
                ('college_university', models.CharField(max_length=200)),
                ('college_address', models.CharField(max_length=200)),
                ('college_contact', models.CharField(max_length=200)),
                ('doc', models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 23, 38, 498977))),
                ('slug', models.SlugField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam_id', models.AutoField(primary_key=True, serialize=False)),
                ('exam_name', models.CharField(max_length=100)),
                ('instructions', models.CharField(blank=True, max_length=2000)),
                ('duration', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('starting_time', models.CharField(max_length=100)),
                ('ending_time', models.CharField(max_length=100)),
                ('doc', models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 23, 38, 505958))),
                ('slug', models.SlugField()),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.college')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_code', models.CharField(max_length=100)),
                ('total_marks', models.CharField(max_length=100)),
                ('doc', models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 23, 38, 501970))),
                ('slug', models.SlugField()),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='App.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=200)),
                ('student_email', models.EmailField(max_length=254)),
                ('student_phone', models.CharField(max_length=50)),
                ('student_address', models.CharField(max_length=200)),
                ('session', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('student_password', models.CharField(max_length=100)),
                ('doc', models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 23, 38, 503964))),
                ('slug', models.SlugField()),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='App.branch')),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.college')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('questions', models.CharField(max_length=2000)),
                ('option_a', models.CharField(max_length=200)),
                ('option_b', models.CharField(max_length=200)),
                ('option_c', models.CharField(max_length=200)),
                ('option_d', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
                ('marks', models.CharField(max_length=200)),
                ('section', models.CharField(choices=[('all', 'All'), ('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'), ('f', 'F'), ('g', 'G')], max_length=100)),
                ('doc', models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 23, 38, 508949))),
                ('slug', models.SlugField()),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='App.branch')),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.college')),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='App.exam')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='App.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Proctor',
            fields=[
                ('proctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('proctor_name', models.CharField(max_length=100)),
                ('proctor_email', models.CharField(max_length=100)),
                ('proctor_phone', models.CharField(max_length=100)),
                ('proctor_password', models.CharField(max_length=100)),
                ('doc', models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 23, 38, 502966))),
                ('slug', models.SlugField()),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.college')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='proctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='App.proctor'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='App.subject'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=200)),
                ('doc', models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 8, 15, 23, 38, 509948))),
                ('slug', models.SlugField()),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='question', to='App.questions')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='App.students')),
            ],
        ),
    ]