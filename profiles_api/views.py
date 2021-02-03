from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from profiles_api import serializers
from profiles_api import models



class TestApiView(APIView):
    """Test API view"""
    def get(self,request,format=None):
        """Return a List of test APIViews"""
        fruits_list = []
        for i in range(10):
            fruits_list.append("Kutta")
        return Response({'message':'Le baba aam kha','data':fruits_list})


class UserProfileViewSets(viewsets.ModelViewSet):
    """Handling for creating and updating user profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
