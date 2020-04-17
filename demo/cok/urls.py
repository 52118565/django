from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^cok', views.cok),
    re_path(r'getcok', views.getcok),
]