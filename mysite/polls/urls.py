from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name="results"),
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),
]

urlpatterns += staticfiles_urlpatterns()