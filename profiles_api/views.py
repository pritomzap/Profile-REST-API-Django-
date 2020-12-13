from rest_framework.views import APIView
from rest_framework.response import Response

class TestApiView(APIView):
    """Test API view"""
    def get(self,request,format=None):
        """Return a List of test APIViews"""
        fruits_list = []
        for i in range(10):
            fruits_list.append("Mango")
        return Response({'message':'Le baba aam kha','data':fruits_list})
