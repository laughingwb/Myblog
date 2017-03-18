
from django.conf.urls import url
from . import views as mylife_views

urlpatterns = [
    url(r'^home/$', mylife_views.showHome, name='showHome'),
    url(r'^lifelist/$', mylife_views.lifelist, name='lifelist'),
    url(r'^addtype/$', mylife_views.addtype, name='addtype'),
    url(r'^addAricle/$', mylife_views.addAricle, name='addAricle'),
    url(r'^subtracttype/$', mylife_views.subtracttype, name='subtracttype'),
]