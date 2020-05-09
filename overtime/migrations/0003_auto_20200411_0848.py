# Generated by Django 3.0 on 2020-04-11 05:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('overtime', '0002_overtimeplan_overtimeschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overtimeschedule',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='overtimeschedule',
            name='start_time',
        ),
        migrations.AddField(
            model_name='overtimeschedule',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='overtimeschedule',
            name='number_of_hours',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='overtimeplan',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]