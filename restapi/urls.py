from django.conf.urls import url
from restapi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^tasks/$', views.TaskList.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view()),
    url(r'^category/$', views.CategoryList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
])
