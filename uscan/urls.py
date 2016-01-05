"""uscan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from goodie import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
#   url(r'^request/', views.event_request, name='eventrequest'),
    url(r'^check/(?P<event_code>\w+)/', views.check_event),
    url(r'^manual/(?P<event>\w+)/',views.manual_register, name='manualregister'),
    url(r'^register/(?P<event>\w+)/(?P<matric_number>\w+)', views.register, name='register'),
    url(r'^list/(?P<event>\w+)/', views.list_matric),
]
