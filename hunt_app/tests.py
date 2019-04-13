from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
import inspect

from . import views
from . import models

class ApiPageTest(TestCase):

    def test_api_status_code(self):
        response = self.client.get('/api/')
        self.assertEquals(response.status_code, 200)

class SignupPageTest(TestCase):

    def test_signup_status_code(self):
        response = self.client.get('/api/signup/')
        self.assertEquals(response.status_code, 200)

class CheckpointPageTest(TestCase):

    def test_checkpoint_status_code(self):
        response = self.client.get('/api/checkpoint/')
        self.assertEquals(response.status_code, 200)

class HuntPageTest(TestCase):

    def test_hunt_status_code(self):
        response = self.client.get('/api/hunt/')
        self.assertEquals(response.status_code, 200)

class UserHuntPageTest(TestCase):

    def test_userhunt_status_code(self):
        response = self.client.get('/api/userhunt/')
        self.assertEquals(response.status_code, 200)

class UserImagesPageTest(TestCase):

    def test_userimages_status_code(self):
        response = self.client.get('/api/userimages/')
        self.assertEquals(response.status_code, 200)

class HuntClassTest(TestCase):

    def test_hunt_class(self):
        hunt = models.Hunt
        self.assertTrue(inspect.isclass(hunt))

class CheckpointClassTest(TestCase):

    def test_checkpoint_class(self):
        checkpoint = models.Checkpoint
        self.assertTrue(inspect.isclass(checkpoint))

class UserHuntClassTest(TestCase):

    def test_hunt_class(self):
        userhunt = models.UserHunt
        self.assertTrue(inspect.isclass(userhunt))

class UserCheckpointImageTest(TestCase):

    def test_usercheckpointimage_class(self):
        usercheckpointimage = models.UserCheckpointImage
        self.assertTrue(inspect.isclass(usercheckpointimage))

