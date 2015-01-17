from django.conf.urls import patterns, url

from houseman import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<appliance_id>\d+)/$', views.switch, name='switch'),
)
