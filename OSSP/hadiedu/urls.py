from django.contrib import admin
from django.conf.urls import url
from . import views


app_name = 'handi'
urlpatterns = [
    url('index',views.index ),
    url('search', views.input, name = 'search')
]
