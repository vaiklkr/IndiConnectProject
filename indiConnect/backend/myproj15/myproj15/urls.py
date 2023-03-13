
from django.contrib import admin
from django.urls import path,re_path
from CustomerApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^CustomerApp$',views.cust_input)
]
