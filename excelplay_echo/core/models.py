from django.db import models
from django.utils import timezone

# userid will be changed to ONe to One to User auth object
class Echouser(models.Model):
	userid = models.IntegerField(primary_key=True,on_delete=models.CASCADE)
	points = models.IntegerField()
	rank = models.IntegerField()
	def __str__(self):
		return self.userid


class Problems(models.Model):
	pid = models.IntegerField(primary_key=True,on_delete=models.CASCADE)
	ptext = models.CharField(max_characters=256)
	def __str__(self):
		return self.pid

class EchoUserSubmission(models.Model):
	userid = models.ForeignKey(Echouser,on_delete=models.CASCADE)
	pid = models.ForeignKey(Problems,on_delete=models.CASCADE)
	files = models.FileField(null=True)
	sub_time = models.DateTimeField(auto_now_add=True,blank=True)
	sub_text = models.CharField(null=True,max_length=True)
