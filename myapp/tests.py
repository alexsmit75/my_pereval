from django.test import TestCase
import unittest
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from pereval.models import Pereval, User, Coords, Level, Image


class TestMyApp(unittest.TestCase):
    pass


class TestApp(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('password')
        self.user.save()
        self.coord = Coords.objects.create(latitude=55.7558, longitude=37.6173)
        self.level = Level.objects.create(name='Test Level')
        self.image = Image.objects.create(url='https://example.com/image.jpg')
        self.pereval_data = {
            "user": self.user.pk,
            "coord": self.coord.pk,
            "level": self.level.pk,
            "images": self.image.pk,
            "status": "new",
            "beauty_title": "Test Beauty Title",
            "title": "Test Title",
            "other_titles": "Test Other Titles",
            "connect": "Test Connect"
        }

    def test_submit_data(self):
        url = reverse('submit-data')
        response = self.client.post(url, self.pereval_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_data(self):
        pereval = Pereval.objects.create(user=self.user, coord=self.coord, level=self.level, images=self.image, status="new")
        url = reverse('get-data', args=[pereval.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_data(self):
        pereval = Pereval.objects.create(user=self.user, coord=self.coord, level=self.level, images=self.image, status="new", beauty_title="Test Beauty Title", title="Test Title", other_titles="Test Other Titles", connect="Test Connect")
        url = reverse('update-data', args=[pereval.pk])
        response = self.client.patch(url, {"beauty_title": "Updated Test Beauty Title"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
