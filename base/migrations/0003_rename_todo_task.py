# Generated by Django 3.2.9 on 2022-03-12 13:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_rename_task_todos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Task',
        ),
    ]
