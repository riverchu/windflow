from django.urls import path, include

from . import views

app_name = 'armory'
urlpatterns = [
    path('', views.manage, name='manage'),
]
