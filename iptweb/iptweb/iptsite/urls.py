from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^history$', views.history, name='history'),
    url(r'^run$', views.run, name='run'),
    url(r'^help$', views.help, name='help'),
    url(r'^compile$', views.compile, name='compile'),
	url(r'^login$', views.login, name='login'),

]
