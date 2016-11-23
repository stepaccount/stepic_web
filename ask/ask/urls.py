# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mainroot', name = 'mainroot'),
    url(r'^login/.*$', 'user_login', name = 'user_login'),
    url(r'^signup/.*$', 'signup', name = 'signup'),
    url(r'^question/(?P<id>[0-9]+)/$', 'question', name = 'question'),
    url(r'^ask/.*$', 'new_ask', name = 'ask'),
    url(r'^popular/.*$', 'popular', name = 'polular'),
    url(r'^new/.*$', 'test', name = 'new'),
    url(r'^answer/.*$', 'add_answer', name = 'add_answer'),
)

