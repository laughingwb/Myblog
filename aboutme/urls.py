from django.conf.urls import url
from . import views as aboutme_views

urlpatterns = [
    url(r'^aboutme/$', aboutme_views.myselfinfo, name='myselfinfo'),
]