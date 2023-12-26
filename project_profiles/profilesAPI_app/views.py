from rest_framework.views import APIView
from rest_framework.response import Response

class helloapi(APIView):
    def get(self, request, format = None):
        an_apiview = [
            'uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to traditional django view',
            'Gives you the most control on your application logic',
            'is mapped manually to URLs'
        ]
        return Response({'message':'hello','an_apiview':an_apiview})
    