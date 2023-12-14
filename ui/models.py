from typing import Any
from django.db import models

# Create your models here.
# class Person(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     age = models.IntegerField(null=True)
#     date = models.DateField(auto_now_add=True)
#     pass

#     def __str__(self) -> str:
#         return self.name
    
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username
 
   
class Calculate_Data(models.Model):
    id
    username        = models.CharField(max_length=150)
    ph              = models.CharField(max_length=150)
    ssa             = models.CharField(max_length=150)
    id_ig_ratio     = models.CharField(max_length=150)
    nitrogen        = models.CharField(max_length=150)
    oxygen          = models.CharField(max_length=150)
    sulphur         = models.CharField(max_length=150)
    density         = models.CharField(max_length=150)
    predicted_value = models.CharField(max_length=150)