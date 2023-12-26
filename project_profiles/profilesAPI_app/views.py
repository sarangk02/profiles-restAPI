from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework import status
from . import serializers

# apiview 
class helloapi(APIView):
    serializer_class = serializers.HelloSerializer
    def get(self, request, format = None):
        an_apiview = [
            'uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to traditional django view',
            'Gives you the most control on your application logic',
            'is mapped manually to URLs'
        ]
        return Response({'message':'hello','an_apiview':an_apiview})
    
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'Hey {name}!!!'
            return Response({'message':msg})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk = None):
        return Response({'method':'PUT'})
    def patch(self,request,pk = None):
        return Response({'method':'PATCH'})
    def delete(self,request,pk = None):
        return Response({'method':'DELETE'})
    
# viewsets 
class helloviewset(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    # http GET 
    def list(self,request):
        return Response({'message':'Hola nigglet'})
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'Hey {name}!!!'
            return Response({'message':msg})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)