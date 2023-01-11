from django.contrib import admin
from django.urls import path, re_path, include
from .views import MessageCreateAPI, GetTokenAPI


urlpatterns = [
    path('api/v1/messages/', MessageCreateAPI.as_view()),
    path('api/v1/get_token/', GetTokenAPI.as_view()),
]
