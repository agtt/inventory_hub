from django.conf.urls.defaults import *
 
urlpatterns = patterns('home.views',
    url(r'^$', 'index', name='index'),
    url(r'^search/$', 'search', name='search'),
)

