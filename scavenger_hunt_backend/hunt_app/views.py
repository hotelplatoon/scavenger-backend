from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    'Test API view'

    def get(self, request, format=None): #  returns list of APIList features

      an_apiview = [
        'Uses HTTP methods as functions (get,post,patch,put,delete)'
        'It is similar to a traditional Django view'
        'Gives you the most control over your logic'
        'Is mapped manually to URLs'
      ]

      return Response({'message': 'Hello!', 'an_apiview': an_apiview})