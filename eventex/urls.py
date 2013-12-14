from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^inscricao/',include('eventex.subscriptions.urls',namespace='subscriptions')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'',include('eventex.core.urls', namespace='core')),
)
