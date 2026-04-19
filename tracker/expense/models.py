from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    age = models.IntegerField(blank=True,null=True)
    location = models.CharField(max_length=100,null=True,blank=True)

class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateField()

