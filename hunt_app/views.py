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

class UserProfileViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=name', '=email',)

class LoginViewSet(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)
        
class HuntViewSet(viewsets.ModelViewSet):
    queryset = models.Hunt.objects.all()
    serializer_class = serializers.HuntSerializer

class CheckpointViewSet(viewsets.ModelViewSet):
    queryset = models.Checkpoint.objects.all()
    serializer_class = serializers.CheckpointSerializer

class UserHuntViewSet(viewsets.ModelViewSet):
    queryset = models.UserHunt.objects.all()
    serializer_class = serializers.UserHuntSerializer

class UserCheckpointImageViewSet(viewsets.ModelViewSet):
    queryset = models.UserCheckpointImage.objects.all()
    serializer_class = serializers.UserCheckpointImageSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=user_hunt_id', '=user_id',)