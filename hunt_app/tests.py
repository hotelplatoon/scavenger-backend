from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from . import views

class ApiPageTest(SimpleTestCase):

    def test_api_status_code(self):
        response = self.client.get('/api/')
        self.assertEquals(response.status_code, 200)