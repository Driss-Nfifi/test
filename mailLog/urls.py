from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('tablemaillog', views.tablemaillog,name="tablemaillog"),

]