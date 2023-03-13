"""indiConnect_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from indiConnectApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^indiConnect$',views.input),
    re_path('^sign$',views.sign),
    re_path('^insert$',views.insert),
    re_path('^send_otp$',views.send_otp),
    re_path('^verified$',views.verified),
    re_path('^verification_done$',views.verification_done),

]
