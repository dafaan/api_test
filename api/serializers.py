from rest_framework import serializers
from etapp.models import item
from django.contrib.auth.models import User

class itemserializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'
        
        

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'