# Generated by Django 3.0.7 on 2020-10-02 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_statutorydeduction'),
        ('leave', '0005_auto_20200810_1122'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Leave_Records',
            new_name='LeaveRecord',
        ),
    ]