from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from . import views

class ApiPageTest(TestCase):

    def test_api_status_code(self):
        response = self.client.get('/api/')
        self.assertEquals(response.status_code, 200)

class SignupPageTest(TestCase):

    def test_api_status_code(self):
        response = self.client.get('/api/signup/')
        self.assertEquals(response.status_code, 200)

# class ApiPageTest(SimpleTestCase):

#     def test_api_status_code(self):
#         response = self.client.get('/api/')
#         self.assertEquals(response.status_code, 200)

# class ApiPageTest(SimpleTestCase):

#     def test_api_status_code(self):
#         response = self.client.get('/api/')
#         self.assertEquals(response.status_code, 200)

# class ApiPageTest(SimpleTestCase):

#     def test_api_status_code(self):
#         response = self.client.get('/api/')
#         self.assertEquals(response.status_code, 200)
