# Generated by Django 4.2.5 on 2023-10-05 18:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_alter_priority_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='task_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
