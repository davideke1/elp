from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length =  400)
    confirm_password = serializers.CharField(max_length =  400)
    class Meta:
        model = User
        fields = ['firts_name','other_names','email','contact','password','confirm_password','gender','location']
        

    