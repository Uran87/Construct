from django.contrib import admin
from django.urls import path, include
from construct import views
from Construction import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('fences', views.fences, name='fences'),
    path('', views.my_main_page, name='my_main_page'),


    path('<str:city>', views.my_main_page, name='my_main_page'),
    path('fences/<str:city>/', views.fences, name='fences_city'),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
