from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("", views.main),
    path("mp4/", views.mp4),
    path("mp4/<str:textID>", views.mp4Details),
    
]