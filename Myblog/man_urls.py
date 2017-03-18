from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from aboutme import views as aboutme_views
from mylife import views as mylife_views
urlpatterns = [
    url(r'^$', aboutme_views.man_home, name='man_home'),
    url(r'^lifemanage/$', mylife_views.lifemanage, name='lifemanage'),
    url(r'^loginout/$', aboutme_views.loginout, name='loginout'),
    url(r'^techmanage/$', aboutme_views.techmanage, name='techmanage'),
    url(r'^myinfomanage/$', aboutme_views.myinfomanage, name='techmanage'),
    url(r'^messagemanage/$', aboutme_views.messagemanage, name='techmanage'),
]
