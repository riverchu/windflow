from django.urls import path, include

from . import views

app_name = 'info'
urlpatterns = [
    path('', views.show, name='show'),
]
