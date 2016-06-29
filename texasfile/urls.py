from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<resource_number>[^/]+)/$', views.index, name='index'),
    ]
