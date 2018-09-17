from django.db import models
from django.utils import timezone

# userid will be changed to OneToOneField on integration with Auth.


class EchoUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    points = models.IntegerField()
    rank = models.IntegerField()

    def __repr__(self):
        return self.userid

    class Meta:
        ordering = ['user_id','-points']

class EchoUserSubmission(models.Model):
    user_id = models.ForeignKey(EchoUser, on_delete=models.CASCADE)
    files = models.FileField(null=True)
    submission_time = models.DateTimeField(auto_now_add=True, blank=True)
    submission_text = models.TextField(null=True, max_length=10000)

class Problems(models.Model):
    pid = models.IntegerField(primary_key=True)
    problem_statement = models.TextField()
