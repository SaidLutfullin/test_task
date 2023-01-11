from django.contrib import admin
from django.urls import path, re_path, include

#from women.views import *

urlpatterns = [
    path('api/v1/authentication/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth-token/', include('djoser.urls.authtoken')),
]
