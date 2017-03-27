"""Myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.conf.urls.static import static
from mylife import views as mylife_views
from aboutme import views as aboutme_views
from message import views as message_views
from . import  man_urls
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', mylife_views.showHome, name='showHome'),
    url(r'^mylife/', include('mylife.urls')),
    url(r'^aboutme/', include('aboutme.urls')),
    url(r'^message/', include('message.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^man/', include(man_urls)),
    url(r'^login/', aboutme_views.login_man, name='login_man'),
    url(r'^login/', auth_views.login),
]+ static(settings.STATIC_URL) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
