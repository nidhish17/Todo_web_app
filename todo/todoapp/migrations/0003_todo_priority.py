# Generated by Django 4.2.5 on 2023-09-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_rename_task_creaated_todo_task_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(1, '⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐')], null=True),
        ),
    ]
