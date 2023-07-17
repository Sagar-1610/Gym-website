from django.db import models


# Create your models here.


class EnquiryModels(models.Model):
    Sr_no = models.AutoField(primary_key=True)
    Gender = models.CharField(max_length=50,choices=(("Male","Male"),("Female","Female")))
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Phone = models.BigIntegerField()
    email_address = models.CharField(max_length=60)
    City = models.CharField(max_length=80)
    our_packages = models.CharField(max_length=70,choices=(("Platinum","Platinum"),("Gold","Gold"),("Silver","Silver"),("Bronze","Bronze")))

