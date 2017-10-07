"""meine-stadt-transparent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from elasticsearch_admin.views import index as elasticsearch_admin

from meine_stadt_transparent.settings import ELASTICSEARCH_URL_PUBLIC

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^elasticsearch_admin/', elasticsearch_admin, {'url': ELASTICSEARCH_URL_PUBLIC}, name='index'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('mainapp.urls')),
]