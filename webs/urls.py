from django.conf.urls import patterns, url
 
from webs import views
 
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<snippet_id>\d+)/$', views.detail, name='detail'),
    url(r'^form', views.form, name='post'),
    url(r'^post', views.post_form, name='post'),
)