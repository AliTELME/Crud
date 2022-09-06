# from pyexpat import model
from django.db import models

# Create your models here.


class Student_list(models.Model):
    F_Name = models.CharField(max_length=100)
    L_Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)