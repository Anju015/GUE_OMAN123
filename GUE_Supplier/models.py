from django.db import models

# Create your models here.


# # Supplier Registration .....
class supplier_reg_table(models.Model):
    supName=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    payment=models.DecimalField(max_digits=9,decimal_places=2)