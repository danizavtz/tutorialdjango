# coding: utf-8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('eventex.core.views',
    url(r'^$', 'home', name='home'),
)
