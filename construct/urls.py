from django.contrib import admin
from django.urls import path, include
from construct import views
from Construction import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('modal_form', views.modal_form, name='modal_form'),
    path('fences', views.fences, name='fences'),

    #path('<str:city>', views.my_main_page, name='my_main_page'),
    path('fences/<str:city>/', views.fences, name='fences_city'),

    path('', views.my_main_page, name='my_main_page'),
    path('video', views.video, name='videopage'),
    path('video/<str:slug>/', views.video_detail, name='videopage_detail'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)