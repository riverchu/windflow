from django.urls import path, include

from . import views

app_name = 'attack'
urlpatterns = [
    path('', views.manage, name='manage'),
]
