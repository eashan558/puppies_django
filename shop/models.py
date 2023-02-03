from django.db import models

# Create your models here.
class product(models.Model):
    pname=models.CharField(max_length=50)
    ptype=models.CharField(max_length=50)
    dateadded=models.DateField()
