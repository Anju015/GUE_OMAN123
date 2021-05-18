# Generated by Django 3.2 on 2021-05-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='supplier_reg_tbl1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supName', models.CharField(max_length=100)),
                ('pdtId', models.CharField(max_length=100)),
                ('pdtName', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('payment', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
    ]
