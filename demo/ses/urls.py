from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path(r'setses/', views.setses),
    re_path(r'^getses/', views.getses),
]