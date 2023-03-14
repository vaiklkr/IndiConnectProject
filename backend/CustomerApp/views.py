from django.shortcuts import render
from CustomerApp.models import Cust
# Create your views here.

def cust_input(request):
    custs = Cust.objects.all()
    return render(request,'base.html',{'cust_d':custs})
