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
    contact = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    incomming = models.TextField(blank=True, null=True)
    outgoing = models.TextField(blank=True, null=True)
    facebook = models.TextField(blank=True, null=True)
    whatsapp = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.devicename
