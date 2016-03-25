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
    url(r'^answer/(?P<pk>\d+)/upvote/$', views.upvote_create_view, name='upvote_create_view'),
    url(r'^answer/(?P<pk>\d+)/downvote/$', views.downvote_create_view, name='downvote_create_view'),
    url(r'^api/questions/$', views.QuestionListCreateAPIView.as_view(), name='question_list_create_view'),
    url(r'^api/answers/$', views.AnswerListCreateAPIView.as_view(), name='answer_list_create_view'),
    url(r'^api/tags/$', views.TagListCreateAPIView.as_view(), name='tag_list_create_view'),
    url(r'^api/votes/$', views.VoteListCreateAPIView.as_view(), name='vote_list_create_view'),
    url(r'^api/questions/(?P<pk>\d+)/$', views.QuestionRetrieveUpdateDestroyAPIView.as_view(), name='question_retrieve_update_destroy_view'),
    url(r'^api/answers/(?P<pk>\d+)/$', views.AnswerRetrieveUpdateDestroyAPIView.as_view(), name='answer_retrieve_update_destroy_view'),
    url(r'^api/posts/(?P<pk>\d+)/$', views.TagRetrieveUpdateDestroyAPIView.as_view(), name='tag_retrieve_update_destroy_view'),
    url(r'^api/votes/(?P<pk>\d+)/$', views.VoteRetrieveUpdateDestroyAPIView.as_view(), name='vote_retrieve_update_destroy_view')
]
