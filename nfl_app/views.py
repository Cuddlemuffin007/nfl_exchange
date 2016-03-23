from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, DetailView
from django.core.urlresolvers import reverse
from nfl_app.models import UserProfile, Question, Answer, Tag


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
        context['quesion_answers'] = Answer.objects.filter(question=self.kwargs.get('pk'))
        print(context)
        return context
