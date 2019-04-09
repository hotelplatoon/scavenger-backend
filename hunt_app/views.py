from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions

class UserProfileViewSet(viewsets.ModelViewSet):   # handles creating, reading, updating profiles
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet): #  checks email and password and returns an auth token

    serializer_class = AuthTokenSerializer

    def create(self, request):  # use the obtain auth token api view to validate and create a token
        return ObtainAuthToken().post(request)

class CheckpointViewSet(viewsets.ViewSet):
  queryset = User.objects.all()
  serializer_class = CheckpointSerializer

class HuntViewSet(viewsets.ViewSet):
  queryset = User.objects.all()
  serializer_class = HuntSerializer

class UserhuntViewSet(viewsets.ViewSet):
  queryset = User.objects.all()
  serializer_class = UserhuntSerializer

class UserViewSet(viewsets.ViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer