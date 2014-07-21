from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = patterns('',
    url(r'^$', views.SnippetList.as_view(), name='snippets'),
    url(r'^(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippets'),
)

urlpatterns = format_suffix_patterns(urlpatterns)