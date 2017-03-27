from django.conf.urls import url
from . import views as message_views

urlpatterns = [
    url(r'^showmessage/$', message_views.showmessage, name='showmessage'),
    # url(r'^lifelist/$', message_views.lifelist, name='lifelist'),
]