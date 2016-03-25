from django.db import models
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    score = models.IntegerField(default=0)


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
    poster = models.ForeignKey('auth.User')
    posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted']


class Answer(models.Model):
    body = models.TextField()
    score = models.IntegerField(default=0)
    poster = models.ForeignKey('auth.User')
    question = models.ForeignKey(Question)
    posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score', '-posted']


class Vote(models.Model):
    voter = models.ForeignKey('auth.User')
    answer = models.ForeignKey(Answer)
    value = models.IntegerField(default=0)


@receiver(post_save, sender='auth.User')
def create_user_profile(sender, **kwargs):
    user_instance = kwargs.get('instance')
    if kwargs.get('created'):
        UserProfile.objects.create(user=user_instance)
        Token.objects.create(user=user_instance)


@receiver(post_save, sender=Question)
def increment_user_score(sender, **kwargs):
    question_instance = kwargs.get('instance')
    if kwargs.get('created'):
        question_instance.poster.userprofile.score += 5
        question_instance.poster.userprofile.save()


@receiver(post_save, sender=Vote)
def assign_points(sender, **kwargs):
    vote_instance = kwargs.get('instance')
    answer = vote_instance.answer
    userprofile = answer.poster.userprofile
    if vote_instance.value == 1:
        userprofile.score += 10
    elif vote_instance.value == -1:
        userprofile.score -= 5
    userprofile.save()

    answer_upvotes = Vote.objects.filter(answer=answer, value=1).count()
    answer_downvotes = Vote.objects.filter(answer=answer, value=-1).count()
    answer.score = answer_upvotes - answer_downvotes
    answer.save()
