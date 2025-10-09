from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class BookTests(APITestCase):
    
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="nabanita_test", password="1234"
        )

        # Generate JWT token for the user
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        # Set credentials for all requests
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

    def test_books_list(self):
        url = reverse('book-list')  # comes from your router
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_books_create(self):
        url = reverse('book-list')  # comes from your router
        data = {"title": "ABC", "author": "XYZ", "published_date": "2025-01-01",
                "isbn": "TYXSER"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)