from django.contrib import messages
from django.shortcuts import render
from .models import users
from django.http import HttpResponse
from django.shortcuts import redirect
import json
import time

def input(request):
    return render(request, 'signin.html')

def sign(request):
    if request.method == 'POST':
        user_obj = users.objects.all()  #if u want display all objects
        user_n = request.POST.get('user_txt')
        pass_w = request.POST.get('pass_txt')
        
        try:
            registered_user = users.objects.get(user_name=user_n)
            if pass_w == registered_user.pass_word:
                messages.success(request, "Success")
                print("login success")
                dict1 = {'user':registered_user,'pwd':registered_user.pass_word}                
                str1 = "successfully logged in with " + user_n + " and " + registered_user.pass_word + ""
                #return HttpResponse(str1)
                return render(request,'otp_ver.html')
            else:
                messages.error(request,'Wrong Password')
                return HttpResponse("wrong Password")
                #return render(request,'signin.html')
        except users.DoesNotExist:
            messages.error(request, "Username does not exists")
            return HttpResponse("Username does not exists")    
    #else:
    #    return render(request, 'signin.html')
    
def insert(request):
    
        import pymysql
        con = pymysql.connect(host='localhost', user='root', password='root', db='indiConnect')
        cur = con.cursor()
        if request.method == 'POST':
            f_name = request.POST.get('fname')
            m_name = request.POST.get('mname')
            l_name = request.POST.get('lname')
            m_mob = request.POST.get('mobno')
            em_id = request.POST.get('emailid')
            user_data = users(user_name=f_name, pass_word=m_mob, fname=f_name, mname=m_name, lname=l_name, mob_no=m_mob, email_id=em_id, otp=120)
            user_data.save()
            return render(request,'signin.html')    
            
        else:
            return render(request, 'signup.html')
        
        
    
def send_otp(request):
    return render(request, 'otp_ver.html')

def verified(request):
    if request.method == 'POST':
        #return HttpResponse("Return to same page")
        mob = request.POST.get('n1')
        import random
        import math
        digits = '0123456789'
        
    else:
        return render(request,'otp_ver.html')

def verification_done(request):
    if request.method == 'POST':
        return render(request,'main_dashboard')