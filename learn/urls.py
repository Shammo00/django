from django.urls import path
from django.contrib import admin
from django.conf.urls import include
app_name = 'learn'
from . import views
urlpatterns = [
    path('',views.home , name='home'),
    path('admin/',include('ca.urls')), 
    path('topics/',views.topics , name='topics'),
    path('topics/<int:topic_id>/',views.topic , name='topic'),
    path('new_topic/',views.new_topic , name='new_topic'),
    path('topic/<int:topic_id>/add_entry/', views.add_entry, name='add_entry'),
]

