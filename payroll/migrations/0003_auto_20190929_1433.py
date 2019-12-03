# Generated by Django 2.2.2 on 2019-09-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0002_auto_20190927_0841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payslip',
            name='bonus',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='total_nssf_contrib',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='total_statutory',
        ),
        migrations.AlterField(
            model_name='payslip',
            name='damage_deduction',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='employee_nssf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='employer_nssf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='gross_salary',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='net_salary',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='overtime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='paye',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='sacco_deduction',
            field=models.IntegerField(),
        ),
    ]
