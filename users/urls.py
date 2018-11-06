from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [

    path('usr/',include('rest_auth.urls')),
    path('usr/rg/',include('rest_auth.registration.urls')),


]