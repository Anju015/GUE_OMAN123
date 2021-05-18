from django.db import models

# Create your models here.
# # customer feedback
class cust_feedback_tbl(models.Model):
    custname=models.CharField(max_length=100)
    comments=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
##customer registration
class cust_reg_tbl(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    uname=models.CharField(max_length=100)
    password1=models.CharField(max_length=100)