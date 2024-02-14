from django.db import models
from registration.models import CustomUser

class Poll(models.Model):
    question_text = models.CharField(max_length=255)


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    voters = models.ManyToManyField(CustomUser, blank=True, null=True)
