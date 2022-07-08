from turtle import mode
from xml.parsers.expat import model
from django.db import models
from datetime import datetime    

# Create your models here.

class Amtdep(models.Model):
    acc = models.CharField(max_length=8)
    date = models.DateTimeField(default=datetime.now(), blank=True)





class Amtfer(models.Model):
    name = models.CharField(max_length=225)
    accno = models.CharField(max_length=15)
    bal =  models.PositiveBigIntegerField()
    date = models.DateTimeField(default=datetime.now(), blank=True)


