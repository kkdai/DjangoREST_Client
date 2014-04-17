from django.conf.urls import patterns, url
 
from webs import views
 
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<snippet_id>\d+)/$', views.detail, name='detail'),
)