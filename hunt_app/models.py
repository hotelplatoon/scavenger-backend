from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.test import TestCase


class UserProfileManager(BaseUserManager): # helps django work with our custom user model
    
    def create_user(self, email, name, password=None):  # creates a new user profile objects
        if not email:
            raise ValueError('Users must have an email address.')
        email = BaseUserManager.normalize_email(email)  # normalizes all emails across the system
        user = self.model(email=email, name=name)
        user.set_password(password) # set_password function encrypts password. converts users password string into a hash in database.
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
        
class UserProfile(AbstractBaseUser, PermissionsMixin):  # represents a user profile in system
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

class Hunt(models.Model):
    category = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    checkpoint_amount = models.IntegerField(serialize=True)
    
    def __str__(self):
        return self.category

class UserHunt(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='users')
    hunt_id = models.ForeignKey(Hunt, on_delete=models.CASCADE, related_name='hunts')
    created_at = models.DateTimeField(default=timezone.now)
    finished_at = models.DateTimeField(default=timezone.now)
        
class Checkpoint(models.Model):
    hunt_id = models.ForeignKey(Hunt, on_delete=models.CASCADE, related_name='hunt')
    clue = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.clue

class UserCheckpointImage(models.Model):
    image_name = models.CharField(max_length=255)
    user_hunt_id = models.ForeignKey(UserHunt, on_delete=models.CASCADE, related_name='userhunts')
    checkpoint_id = models.ForeignKey(Checkpoint, on_delete=models.CASCADE, related_name='checkpoints')
    user_id = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.image_name