from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
#    url(r'^feed_poster/', include('feed_poster.urls')),
    url(r'^snippets/', include('snippets.urls'), name='snippets'),
    url(r'^webs/', include('webs.urls')),
)
