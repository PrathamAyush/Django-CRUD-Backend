from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

#Built-in class for user registration Process
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class TaskSerializer(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source='user.id')  #Read-only field, don't make changes when POST req
    user_detail = UserSerializer(source='user', read_only=True)  #To show the username in response

    class Meta:
        model= Task
        fields=['id', 'title', 'description', 'completed', 'created_at' , 'updated_at' , 'user' , 'user_detail']