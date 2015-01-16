from django.conf.urls import patterns, url

from houseman import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
