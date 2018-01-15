from django.db import models

# Create your models here.

class School(models.Model):

    code = models.CharField(max_length = 1000)
    eduoffice = models.CharField(max_length= 20)
    sname = models.CharField(max_length= 20)
    diff = models.CharField(max_length= 20)
    Enter = models.CharField(max_length= 20)
    parking =  models.CharField(max_length= 20)
    enhi = models.CharField(max_length= 20)
    hallway = models.CharField(max_length= 20)
    hsupport = models.CharField(max_length= 20)
    hfeces = models.CharField(max_length= 20)
    hufine = models.CharField(max_length= 20)
    braille = models.CharField(max_length= 20)
    announce = models.CharField(max_length= 20)
    alarm = models.CharField(max_length= 20)
    address = models.CharField(max_length= 20)
    daddress = models.CharField(max_length= 20)
    pnum = models.CharField(max_length= 20)
    haddress = models.CharField(max_length= 20)
    sex = models.CharField(max_length= 20)
