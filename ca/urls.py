from django.urls import path

from . import views
app_name = 'ca'
urlpatterns = [
    path('',views.admin_login , name='admin_login')
]