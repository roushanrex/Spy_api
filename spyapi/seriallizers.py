from rest_framework import serializers
from .models import User,Phonedata,Audio,Image
#

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Forgetserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class Phonedataserializers(serializers.ModelSerializer):
    class Meta:
        model = Phonedata
        fields = '__all__'


class Audioserializers(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'


class Imageserializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
