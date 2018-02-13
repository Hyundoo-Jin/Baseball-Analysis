from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from bschat import views as bsc

urlpatterns = [
    url(r'^keyboard/', bsc.keyboard)
]
