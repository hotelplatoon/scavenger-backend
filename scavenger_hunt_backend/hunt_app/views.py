from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from django.http import HttpResponse

class HelloApiView(APIView):
    'Test API view'

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None): #  returns list of APIList features

      an_apiview = [
        'Uses HTTP methods as functions (get,post,patch,put,delete)'
        'It is similar to a traditional Django view'
        'Gives you the most control over your logic'
        'Is mapped manually to URLs'
      ]

      return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None): # updates object
        return Response({'method':'put'})

    def patch(self, request, pk=None): # only updates fields required or provided in the request
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):  # test API Viewset  
    def list(self, request):
        a_viewset = [
          'Uses actions (list, create, retrieve, update, partial_update)',
          'Automatically maps to URLs using Routers',
          'Provides more functionality with less code.'
        ]
        return Response({'message':'Hello!', 'a_viewset': a_viewset})
