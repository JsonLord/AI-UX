from django.test import TestCase, Client
from django.urls import reverse

class APIMandatoryTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_health_check(self):
        response = self.client.get(reverse('health_check'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_api_docs(self):
        response = self.client.get(reverse('api_docs'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AI-UX API Documentation")
