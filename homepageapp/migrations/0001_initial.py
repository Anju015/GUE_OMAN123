# Generated by Django 3.2 on 2021-04-13 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('eml', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('uname', models.CharField(max_length=100)),
                ('paswd', models.CharField(max_length=100)),
            ],
        ),
    ]
