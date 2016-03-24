from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from nfl_app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup', views.SignupCreateView.as_view(), name='signup'),
    url(r'^login', auth_views.login, name='login'),
    url(r'^logout', auth_views.logout_then_login, name='logout'),
    url(r'^$', views.QuestionListView.as_view(), name='question_list_view'),
    url(r'^question/(?P<pk>\d+)/$', views.QuestionDetailView.as_view(), name='question_detail_view'),
    url(r'^question/create/$', views.QuestionCreateView.as_view(), name='question_create_view'),
    url(r'^question/(?P<pk>\d+)/post_answer/$', views.AnswerCreateView.as_view(), name='answer_create_view'),
    url(r'^user/(?P<pk>\d+)/$', views.UserProfileDetailView.as_view(), name='user_profile_detail_view'),
]
