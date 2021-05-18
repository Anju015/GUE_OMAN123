# Generated by Django 3.2 on 2021-05-13 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp_reg_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=100)),
                ('dtime', models.DateField(max_length=100)),
                ('empsalary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('uname', models.CharField(max_length=100)),
                ('passwd', models.CharField(max_length=100)),
            ],
        ),
    ]
