from django.urls import path
from django.contrib import admin
from django.conf.urls import include

from . import views
urlpatterns = [
    path('',views.home , name='home'),
    path('admin/',include('ca.urls')), 
    path('topics/',views.topics , name='topics'),
    path('topics/<int:topic_id>/',views.topic , name='topic'),
]
