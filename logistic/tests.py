from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class MyTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_sample_view(self):
        url = '/api/v1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)