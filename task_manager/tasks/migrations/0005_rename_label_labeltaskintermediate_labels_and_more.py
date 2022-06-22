# Generated by Django 4.0.5 on 2022-06-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0004_alter_task_label'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labeltaskintermediate',
            old_name='label',
            new_name='labels',
        ),
        migrations.RemoveField(
            model_name='task',
            name='label',
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='tasks', through='tasks.LabelTaskIntermediate', to='labels.label', verbose_name='Labels'),
        ),
    ]