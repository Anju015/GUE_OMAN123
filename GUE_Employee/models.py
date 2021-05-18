from django.db import models

# Create your models here.

# #employee registration..........
class emp_reg_tbl(models.Model):
    empname=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    dtime=models.DateField(max_length=100)
    empsalary=models.DecimalField(max_digits=9,decimal_places=2)
    uname=models.CharField(max_length=100)
    passwd=models.CharField(max_length=100)

