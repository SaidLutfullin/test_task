from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.authentication.urls')),
    path('', include('applications.telegram_interaction.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
    urlpatterns += re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),