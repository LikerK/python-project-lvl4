# flake8: noqa
# Generated by Django 4.0.4 on 2022-05-29 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labels', '0001_initial'),
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelTaskIntermediate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='labels.label')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=600, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of create')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_author', to=settings.AUTH_USER_MODEL, verbose_name='Auhtor')),
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tasks_executor', to=settings.AUTH_USER_MODEL, verbose_name='Executor')),
                ('label', models.ManyToManyField(blank=True, related_name='tasks', through='tasks.LabelTaskIntermediate', to='labels.label', verbose_name='Labels')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statuses.status', verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Task',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='labeltaskintermediate',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
    ]
