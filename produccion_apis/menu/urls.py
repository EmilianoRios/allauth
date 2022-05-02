from django.contrib import admin
from django.urls import path
from menu import views

urlpatterns = [
    path('',views.menu,name="Menu"),
]