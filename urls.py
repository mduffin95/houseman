from django.conf.urls import patterns, url

from houseman import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='switch'),
    url(r'^(?P<appliance_id>\d+)/process/$', views.process, name='process'),
)
