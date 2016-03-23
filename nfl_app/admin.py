from django.contrib import admin
from nfl_app.models import UserProfile, Question, Tag, Answer


admin.site.register([UserProfile, Question, Tag, Answer])
