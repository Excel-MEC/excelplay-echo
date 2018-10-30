from django.db import models
from django.utils import timezone

# userid will be changed to OneToOneField on integration with Auth.


class EchoUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    pid = models.IntegerField(default=1)
    rank = models.IntegerField()

    def __repr__(self):
        return self.userid

    class Meta:
        ordering = ['user_id','-rank']

class EchoUserSubmission(models.Model):
    pid = models.IntegerField(default=1)
    user_id = models.ForeignKey(EchoUser, on_delete=models.CASCADE)
    files = models.FileField(upload_to='media/')
    submission_time = models.DateTimeField(auto_now_add=True, blank=True)
    submission_text = models.TextField(null=True, max_length=10000)

class Problems(models.Model):
    pid = models.IntegerField(primary_key=True,default=1)
    problem_statement = models.TextField()
