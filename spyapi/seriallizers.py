from rest_framework import serializers
from .models import User,Phonedata

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class Phonedataserializers(serializers.ModelSerializer):
    class Meta:
        model = Phonedata
        fields = '__all__'
