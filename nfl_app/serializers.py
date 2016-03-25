from django.contrib.auth.models import User
from rest_framework import serializers

from nfl_app.models import Question, Answer, Tag, Vote


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
