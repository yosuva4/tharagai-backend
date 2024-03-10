from typing import Any, Dict
from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response

from .products import products

from .serializer import ProductSerializer,UserSerializer,UserSerializerWithToken
from .models import Product


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        print()
        data = super().validate(attrs)
        seriaalizer = UserSerializerWithToken(self.user).data

        for k,v in seriaalizer.items():
            data[k] = v
        return data
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/products/',
        '/products/create/'
    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    serializer = UserSerializer(User.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registerUser(request):
    data = request.data

    print(data)
    message = {}
    if 'username' not in  data or data['username'] == "":
        message['username'] =  "This field is required."
        # return Response(message,status=status.HTTP_400_BAD_REQUEST)
    
    if 'password' not in data or data['password'] == "":
        message['password'] ="This field is required."
        # return Response(message,status=status.HTTP_400_BAD_REQUEST)
    
    if 'email' not in data  or data['email'] == "":
        message['email'] ="This field is required."
        # return Response(message,status=status.HTTP_400_BAD_REQUEST)
    if message:
        return Response(message,status=status.HTTP_400_BAD_REQUEST)

    
    try:
        user = User.objects.create(
            first_name = data['username'],
            username = data['email'],
            email = data['email'],
            password = make_password(data['password']),
        )
        seralizer = UserSerializerWithToken(user,many = False)
        return Response(seralizer.data)
    except:
        message = {'detail':"User with this already exists"}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getProducts(request):
    serializer = ProductSerializer(Product.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request,pk):
    serializer = ProductSerializer(Product.objects.filter(_id=pk),many=True)
    return Response(serializer.data)