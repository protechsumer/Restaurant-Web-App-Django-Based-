from .views import ProfileDetailView

from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^$(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
]