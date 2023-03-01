from django.contrib import admin
from django.urls import path, include
from .models import Fence, Requests, Cities
# Register your models here.

admin.site.register(Fence)
admin.site.register(Requests)
admin.site.register(Cities)
