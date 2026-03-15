from unittest import TestCase


class APIClient:
    pass


class MyTest(TestCase):
    def test(self):
        self.assertTrue(True)

    def test_sample_view(self):
        url = "/api/v1/test/"
        client = APIClient()
        response=client.get(url)
        self.assertEqual(response.status_code,200)
