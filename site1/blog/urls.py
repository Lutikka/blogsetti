
from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /5/
    url(r'^(?P<blogpost_id>[0-9]+)/$', views.detail, name='detail'),
]
