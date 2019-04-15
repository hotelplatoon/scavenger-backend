from rest_framework import serializers
from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only':True}}
    
    def create(self, validated_data):
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class CheckpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Checkpoint
        fields = ['hunt_id','clue','description','image_url','pk']

class HuntSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hunt
        fields = ['category','city', 'checkpoint_amount','pk']

class UserHuntSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserHunt
        fields = ['user_id','hunt_id','created_at','finished_at','pk']

class UserCheckpointImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserCheckpointImage
        fields = ['image_name','user_hunt_id','checkpoint_id','user_id','pk']