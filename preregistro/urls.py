from django.conf.urls import patterns, include, url

from preregistro import views

urlpatterns = patterns('',
	url(r'^$',views.index, name = 'index'),
	url(r'^(?P<curso_id>\d+)$', views.registro, name = 'registro'),
)
