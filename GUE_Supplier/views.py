from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# # Create your views here.
# from . models import reg_tbl

def regsupplier(request):
    return render(request,'Supplier_Reg.html')