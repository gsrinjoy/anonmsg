from msilib.schema import Class
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import IntegerField

# Create your models here.
class Login(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=30)
    slg=models.CharField(max_length=5)
    pas=models.IntegerField

    def __str__(self):
        return (self.website)

class Msgstore(models.Model):
    id=models.AutoField
    txt=models.CharField(max_length=1000)
    slu=models.CharField(max_length=5)