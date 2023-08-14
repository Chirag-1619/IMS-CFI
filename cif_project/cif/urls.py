from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cif' 

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
     path('add-customer/', views.add_customer, name='add_customer'),
     path('', views.homepage, name='homepage'),]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)