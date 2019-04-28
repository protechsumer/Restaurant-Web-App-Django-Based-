"""Restaurants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view
from menus.views import HomeView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view(), name='home'),
    url(r'^register$',RegisterView.as_view(), name='register'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$',activate_user_view, name='activate'),
    url(r'^login/$',LoginView.as_view(), name='login'),
    url(r'^logout/$',LogoutView.as_view(), name='logout'),
    url(r'^profile-follow/$',ProfileFollowToggle.as_view(),name='follow'),
    #url(r'^items/', include('menus.urls', namespace='menus')),
    url(r'^items/', include(('menus.urls', 'menus'), namespace='menus')),
    url(r'^u/', include(('profiles.urls', 'profiles'),namespace='profile')),
    url(r'^restaurants/', include(('restaurants.urls', 'restaurants'), namespace='restaurants')),
    url(r'^about/$',TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$',TemplateView.as_view(template_name='contact.html'), name='contact'),
]
