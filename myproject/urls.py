from django.conf.urls import patterns, include, url
from django.contrib import admin
from myproject.core.views import *

urlpatterns = patterns(
    'myproject.core.views',
    url(r'^$', 'index', name='index'),
    url(r'^morris/$', 'morris', name='morris'),
    url(r'^morris_data/$', MorrisDataView.as_view(), name='morris_data'),
    url(r'^download/$', 'download', name='download'),
    url(r'^about/$', 'about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
)
