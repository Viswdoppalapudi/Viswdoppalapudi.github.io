from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.home, name= "home"),
    path('room/', views.home, name= "home"),

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
