from django.contrib.auth.models import User
from django.db import models


class UserAnswer(models.Model):
    question = models.ForeignKey('Question')
    user = models.ForeignKey(User)
    answer = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Question(models.Model):
    text = models.TextField()
    active = models.BooleanField(default=True)
    users = models.ManyToManyField(User, related_name='questions', through=UserAnswer)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
