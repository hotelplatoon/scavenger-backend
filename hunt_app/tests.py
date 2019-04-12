from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

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

