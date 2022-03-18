from django.contrib import admin
from . models import User,Phonedata,Audio,Image

#
# Register your models here.

admin.site.register(User)
admin.site.register(Phonedata)
admin.site.register(Audio)
admin.site.register(Image)
