from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from rest_framework import serializers
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.exceptions import ValidationError

# Create your views here.
@csrf_exempt
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            if serializer.validated_data.get('password') != serializer.validated_data.get('confirm_password'):
                raise ValidationError('passsword does not match')

            else:
                User.objects.create(
                firts_name=serializer.validated_data.get('firts_name'), email=serializer.validated_data.get('email'),
                other_names = serializer.validated_data.get('other_names'),
                contact = serializer.validated_data.get('contact'), gender = serializer.validated_data.get('gender'), 
                location = serializer.validated_data.get('location'),
                password = make_password(serializer.validated_data.get('password')))
                data = {
                    'status': 'OK',
                    'statu code': status.HTTP_201_CREATED,
                    'data': serializer.data
                }
                return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

