from rest_framework import serializers
from profiles_api import models

class UserProfileSerializer(serializers.ModelSerializer):
    """serializer for a profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style':{'input_type':'password'}
            }
        }
    
    def create(self,validatea_data):
        """Create and returen a new user"""
        user = models.UserProfile.objects.create_user(
            email = validatea_data['email'],
            name = validatea_data['name'],
            password = validatea_data['password']
        )
        return user