from django.db import models
from django.contrib.auth.models import AbstractUser

class users(models.Model):
    user_name = models.CharField(max_length=64)
    pass_word = models.CharField(max_length=64) 
    fname = models.CharField(max_length=64)
    mname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    mob_no = models.BigIntegerField()
    email_id = models.EmailField()
    otp = models.IntegerField()

    def __str__(self):
        return self.user_name