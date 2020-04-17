from django.conf.urls import re_path
from . import views

app_name = "a"

urlpatterns = [
    re_path(r'^resp/', views.resp),
    re_path(r'^js/',views.js),
    re_path(r'^js2/', views.js2, name="j"),
    re_path(r'^tiao/',views.tiao),
]