# Generated by Django 3.1.6 on 2021-03-17 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='task.customer'),
        ),
    ]