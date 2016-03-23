from django.db import models
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    score = models.IntegerField(default=0)


class Tag(models.Model):
    name = models.CharField(max_length=30)


class Question(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
    poster = models.ForeignKey('auth.User')
    posted = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    body = models.TextField()
    score = models.IntegerField(default=0)
    poster = models.ForeignKey('auth.User')
    question = models.ForeignKey(Question)


@receiver(post_save, sender='auth.User')
def create_user_profile(sender, **kwargs):
    user_instance = kwargs.get('instance')
    if kwargs.get('created'):
        UserProfile.objects.create(user=user_instance)
        Token.objects.create(user=user_instance)

