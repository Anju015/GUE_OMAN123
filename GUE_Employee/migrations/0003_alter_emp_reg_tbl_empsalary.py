# Generated by Django 3.2 on 2021-05-13 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GUE_Employee', '0002_alter_emp_reg_tbl_empsalary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp_reg_tbl',
            name='empsalary',
            field=models.CharField(max_length=100),
        ),
    ]