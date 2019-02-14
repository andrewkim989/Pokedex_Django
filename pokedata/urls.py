from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
    url(r'^pokemon/(?P<num>\d+)', views.pokemon)
]