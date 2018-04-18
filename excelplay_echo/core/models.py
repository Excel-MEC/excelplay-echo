from django.db import models
from django.utils import timezone

# userid will be changed to OneToOneField on integration with Auth.


class EchoUser(models.Model):
    user_id = models.IntegerField(primary_key=True, on_delete=models.CASCADE)
    points = models.IntegerField()
    rank = models.IntegerField()

    def __repr__(self):
        return self.userid


class EchoUserSubmission(models.Model):
    user_id = models.ForeignKey(Echouser, on_delete=models.CASCADE)
    pid = models.ForeignKey(Problems, on_delete=models.CASCADE)
    files = models.FileField(null=True)
    sub_time = models.DateTimeField(auto_now_add=True, blank=True)
    sub_text = models.CharField(null=True, max_length=True)
