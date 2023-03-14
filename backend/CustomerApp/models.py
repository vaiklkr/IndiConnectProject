from django.db import models

# Create your models here.
class Cust(models.Model):
    custid = models.IntegerField()
    custname = models.CharField(max_length=20)
    mobile = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    
    def __str__(self):
        return self.custname



