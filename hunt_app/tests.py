from django.db import models
from django.conf import settings
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
import inspect

from . import views
from . import models
from .models import Hunt, UserHunt, Checkpoint, UserCheckpointImage, AbstractBaseUser, BaseUserManager, UserProfileManager, UserProfile

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

class UserProfileClassGetFullNameMethodTest(TestCase):

    def test_userprofile_class_fullname(self):
        method = models.UserProfile.get_full_name
        self.assertTrue(inspect.isfunction(method))

class UserProfileClassGetShortNameMethodTest(TestCase):

    def test_userprofile_class_shortname(self):
        method = models.UserProfile.get_short_name
        self.assertTrue(inspect.isfunction(method))

class UserProfileClassStrEmailMethodTest(TestCase):

    def test_userprofile_class_str_email(self):
        method = models.UserProfile.__str__
        self.assertTrue(inspect.isfunction(method))

class HuntClassCategoryStrMethodTest(TestCase):

    def test_hunt_class_str_category(self):
        method = models.Hunt.__str__
        self.assertTrue(inspect.isfunction(method))

class CheckpointClassStrMethodTest(TestCase):

    def test_checkpoint_class_str_clue(self):
        method = models.Checkpoint.__str__
        self.assertTrue(inspect.isfunction(method))

class UserCheckpointImageStrMethodTest(TestCase):

    def test_checkpoint_class_str_image_name(self):
        method = models.UserCheckpointImage.__str__
        self.assertTrue(inspect.isfunction(method))

class UserProfileManagerCreateUserMethodTest(TestCase):

    def test_userprofilemanager_class_create_user(self):
        method = models.UserProfileManager.create_user
        self.assertTrue(inspect.isfunction(method))

class UserProfileManagerCreateSuperUserMethodTest(TestCase):

    def test_userprofilemanager_class_create_superuser(self):
        method = models.UserProfileManager.create_superuser
        self.assertTrue(inspect.isfunction(method))

class UserProfileManagerInstanceTest(TestCase):

    def test_userprofilemanager_class_instance(self):
        self.assertTrue(isinstance(models.UserProfileManager(),BaseUserManager))

class UserProfileInstanceTest(TestCase):

    def test_userprofile_class_instance(self):
        self.assertTrue(isinstance(models.UserProfile(),AbstractBaseUser))

class HuntClassObjTest(TestCase):

    def create_hunt(self, category='testcategory', city='testcity', checkpoint_amount=1):
        return Hunt.objects.create(category=category, city=city, checkpoint_amount=checkpoint_amount)

    def test_hunt_creation(self):
        hunt = self.create_hunt()
        self.assertTrue(isinstance(hunt, Hunt))  

    def test_hunt_category(self):
        hunt = self.create_hunt()
        self.assertTrue(isinstance(hunt, Hunt))
        self.assertEqual('testcategory', hunt.category)
    
    def test_hunt_city(self):
        hunt = self.create_hunt()
        self.assertTrue(isinstance(hunt, Hunt))
        self.assertEqual('testcity', hunt.city)

    def test_hunt_checkpoint_amount(self):
        hunt = self.create_hunt()
        self.assertTrue(isinstance(hunt, Hunt))
        self.assertEqual(1, hunt.checkpoint_amount)

class CheckpointClassCreationTest(TestCase):

    def create_checkpoint(self, hunt_id=1, clue='this is a test clue', description='test description', image_url='A3h5e45h'):
        hunt_pk = Hunt.objects.create(pk=9, category='testcategory', city='testcity', checkpoint_amount=1)
        checkpoint_obj = Checkpoint.objects.create(hunt_id=hunt_pk, clue=clue, description=description, image_url=image_url)
        return checkpoint_obj

    def test_checkpoint_creation(self):
        checkpoint_obj = self.create_checkpoint()
        self.assertTrue(isinstance(checkpoint_obj, Checkpoint))  

    def test_checkpoint_clue(self):
        checkpoint = self.create_checkpoint()
        self.assertEqual('this is a test clue', checkpoint.clue)

    def test_checkpoint_description(self):
        checkpoint = self.create_checkpoint()
        self.assertEqual('test description', checkpoint.description)

    def test_checkpoint_image_url(self):
        checkpoint = self.create_checkpoint()
        self.assertEqual('A3h5e45h', checkpoint.image_url)