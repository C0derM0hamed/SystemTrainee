from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from trainee.models import Trainee


class TraineeApiTests(APITestCase):
	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username="apiuser",
			password="safe-pass-123",
		)
		self.trainee = Trainee.objects.create(name="Ahmed")

	def test_get_list_allows_anonymous(self):
		response = self.client.get(reverse("api_trainee_list"))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)

	def test_get_detail_allows_anonymous(self):
		response = self.client.get(reverse("api_trainee_detail", args=[self.trainee.id]))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data["name"], "Ahmed")

	def test_get_detail_returns_404_for_missing_id(self):
		response = self.client.get(reverse("api_trainee_detail", args=[99999]))
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_post_requires_authentication(self):
		response = self.client.post(reverse("api_trainee_create"), {"name": "Sara"}, format="json")
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_post_creates_when_authenticated(self):
		self.client.force_authenticate(user=self.user)
		response = self.client.post(reverse("api_trainee_create"), {"name": "Sara"}, format="json")
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertTrue(Trainee.objects.filter(name="Sara").exists())

	def test_post_rejects_whitespace_name(self):
		self.client.force_authenticate(user=self.user)
		response = self.client.post(reverse("api_trainee_create"), {"name": "   "}, format="json")
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertIn("name", response.data)

	def test_put_requires_authentication(self):
		response = self.client.put(
			reverse("api_trainee_update", args=[self.trainee.id]),
			{"name": "Updated"},
			format="json",
		)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_put_updates_when_authenticated(self):
		self.client.force_authenticate(user=self.user)
		response = self.client.put(
			reverse("api_trainee_update", args=[self.trainee.id]),
			{"name": "Updated"},
			format="json",
		)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.trainee.refresh_from_db()
		self.assertEqual(self.trainee.name, "Updated")

	def test_delete_requires_authentication(self):
		response = self.client.delete(reverse("api_trainee_delete", args=[self.trainee.id]))
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_delete_removes_record_when_authenticated(self):
		self.client.force_authenticate(user=self.user)
		response = self.client.delete(reverse("api_trainee_delete", args=[self.trainee.id]))
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertFalse(Trainee.objects.filter(id=self.trainee.id).exists())
