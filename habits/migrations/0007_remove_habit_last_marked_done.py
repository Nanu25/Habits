# Generated by Django 5.1 on 2024-08-18 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0006_habit_last_marked_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='last_marked_done',
        ),
    ]
