from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, DetailView
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
<<<<<<< 5479d1da3e59d4abcd04c863043a86005ccfd148
from django.http import HttpResponseRedirect
=======
>>>>>>> Began apis
from nfl_app.models import UserProfile, Question, Answer, Tag, Vote
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from nfl_app.serializers import QuestionSerializer, AnswerSerializer, TagSerializer, VoteSerializer


class SignupCreateView(CreateView):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login')


class QuestionListView(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question_answers'] = Answer.objects.filter(question=self.kwargs.get('pk'))
        return context


class QuestionCreateView(CreateView):
    model = Question
    fields = ('title', 'body')

    def form_valid(self, form):
        question_object = form.save(commit=False)
        tags = self.request.POST.get('tags').split(',')
        question_object.poster = self.request.user
        question_object.save()
        if any(tags):
            for tag in tags:
                try:
                    new_tag = Tag.objects.get(name=tag)
                except ObjectDoesNotExist:
                    new_tag = Tag.objects.create(name=tag)
                question_object.tags.add(new_tag)
                question_object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('question_detail_view', kwargs={'pk': self.object.pk})


class AnswerCreateView(CreateView):
    model = Answer
    fields = ('body',)

    def form_valid(self, form):
        answer_object = form.save(commit=False)
        answer_object.poster = self.request.user
        answer_object.question = Question.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('question_detail_view', kwargs={'pk': self.kwargs.get('pk')})


class UserProfileDetailView(DetailView):
    model = UserProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_questions'] = Question.objects.filter(poster=context['object'].user)
        return context


def upvote_create_view(request, pk):
    voter = request.user
    answer = Answer.objects.get(pk=pk)
    value = 1
    if answer not in Answer.objects.filter(poster=voter) and not Vote.objects.filter(voter=voter, answer=answer):
        Vote.objects.create(voter=voter, answer=answer, value=value)
    return HttpResponseRedirect('/')


def downvote_create_view(request, pk):
    voter = request.user
    answer = Answer.objects.get(pk=pk)
    value = -1
    if answer not in Answer.objects.filter(poster=voter) and not Vote.objects.filter(voter=voter, answer=answer):
        Vote.objects.create(voter=voter, answer=answer, value=value)
    return HttpResponseRedirect('/')


class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class VoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
