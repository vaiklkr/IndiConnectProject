from django.contrib import admin

# Register your models here.
from CustomerApp.models import Cust

class CustAdmin(admin.ModelAdmin):  #here we are combining Model and Admin bcoz we have to display all objects
    list_display=['custid','custname','mobile','address','city']  #list_display is pre-defined property
admin.site.register(Cust,CustAdmin)    



#(venv) C:\DjangoApps\myproj15>py manage.py makemigrations
#(venv) C:\DjangoApps\myproj15>py manage.py createsuperuser