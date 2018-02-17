from django.contrib import admin
from django.conf.urls import url, include
from bschat import views as bsc

urlpatterns = [
    url(r'^keyboard/', bsc.keyboard),
    url(r'^message', bsc.message)
]
