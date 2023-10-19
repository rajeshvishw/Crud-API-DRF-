from django.contrib import admin
from django.urls import path,include
from mainapp.views import webView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("getdata/",webView.as_view()),
    path("getdata/<int:pk>/",webView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)