from django.test import TestCase
from core.models import EchoUser,EchoUserSubmission

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
