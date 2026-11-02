from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only = True)
    password2 = serializers.CharField(write_only = True)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"password2":"first and second password should be same"})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password1')
        return User.objects.create_user(password = password, **validated_data)
    
class LoginSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ('username','password')
        
    def validate(self, data):
        user = authenticate(
            username = data['username'],
            password = data['password']
        )
        
        if user is None:
            raise serializers.ValidationError({"detail":"invalid username and password"})
        if not user.is_active:
            raise serializers.ValidationError({
                "detail": "This account is inactive."
            })

        data['user'] = user
        return data
        
        
    