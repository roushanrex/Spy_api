from django.db import models



class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phonenumber = models.IntegerField()
    password = models.CharField(max_length=255)
    coupon = models.CharField(max_length=255)
    datetime = models.CharField(max_length=255)
    def __str__(self):
        return self.name




class Phonedata(models.Model):
    email = models.CharField(max_length=255)
    devicename = models.CharField(max_length=255)
    deviceid = models.CharField(max_length=255)
    simnumber = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    contact = models.TextField(blank=True)
    message = models.TextField(blank=True)
    incomming = models.TextField(blank=True)
    outgoing = models.TextField(blank=True)
    facebook = models.TextField(blank=True)
    whatsapp = models.TextField(blank=True)

    def __str__(self):
        return self.devicename
