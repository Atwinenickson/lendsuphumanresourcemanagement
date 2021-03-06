# Generated by Django 3.1.12 on 2021-12-14 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
        ('organisation_details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeKPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure_of_success', models.TextField()),
                ('weight', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('assessor', models.CharField(choices=[('HOD', 'Head of Department'), ('HR', 'Human Resource Officer'), ('Self', 'Self')], max_length=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentKPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure_of_success', models.TextField()),
                ('weight', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation_details.department')),
            ],
        ),
    ]
