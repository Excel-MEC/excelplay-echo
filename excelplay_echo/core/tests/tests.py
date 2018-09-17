from django.test import TestCase,Client
from django.urls import reverse
from core.models import EchoUser,EchoUserSubmission
from rest_framework.test import APIClient,APITestCase
from rest_framework import status

class ModelTests(TestCase):
	def setup(self):
		EchoUser.objects.create(user_id=13,points=0,rank=100)
		EchoUser.objects.create(user_id=100,points=10,rank=90)
		EchoUser.objects.create(user_id=1,points=50,rank=40)
		EchoUserSubmission.objects.create(user_id=13)
		EchoUserSubmission.objects.create(user_id=100)

	def echo_user(self):
		user_a = EchoUser.objects.get(user_id=13)
		user_b = EchoUser.objects.get(user_id=100)
		print(self.assertEqual(user_a.points,0))
		self.assertEqual(user_b.points,10)
		self.assertTrue(isinstance(user_b,EchoUser))
		self.assertEqual(user_a.__repr__(),user_a.user_id)

class leaderboardTests(APITestCase):
	def test_loading_leaderboard(self):
		EchoUser.objects.create(user_id=13,points=10,rank=100)
		client = APIClient()
		url = reverse('leaderboard')
		data = {"user_id": 100,   \
				"points": 543, "rank": 1   }
		response = self.client.get(url,data,format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(EchoUser.objects.get().points,10)


	def test_loading_submit(self):
		client = APIClient()
		url = reverse('finalsubmit')
		data = {
				"id": 7,
				"submission_time": "2018-09-17T01:34:00.164014Z",
				"submission_text": "#!/bin/bash\r\necho \"Hello world\"",
				"user_id": 44
			}
		response = self.client.post(url,data,format='json')
		self.assertEqual(response.status_code,status.HTTP_200_OK)


