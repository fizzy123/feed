from django.conf.urls import patterns, url

from archives import views

urlpatterns = patterns('feed.views',
        url(r'^$', 'display', name='display'),
        url(r'^add_source/$', 'add_source', name='add_source'),
        )
