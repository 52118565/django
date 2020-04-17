from django.conf.urls import  re_path
from . import views

urlpatterns = [
    re_path(r'^request1/', views.request1),
    re_path(r'^request2/(?P<city>[a-z]+)/(?P<year>\d{4})/', views.request2),
    re_path(r'^request3/', views.request3),
    re_path(r'^request4/', views.request4),
    re_path(r'^head/',views.head),
]