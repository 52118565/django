from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^mode/', views.Mode.as_view()),
    re_path(r'^sel/',views.Sel.as_view()),
]