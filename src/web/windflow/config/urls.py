from django.urls import path, include

from . import views

app_name = 'config'
urlpatterns = [
    path('', views.config, name='config'),
]
