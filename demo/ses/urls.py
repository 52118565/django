from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path(r'setses/', views.setses),
    re_path(r'^getses/', views.getses),
    # re_path(r'^rview/', views.Rview.as_view()),
    # 类视图装饰器第二种方法
    # re_path(r'^rview/', views.foo(views.Rview.as_view())),
    re_path(r'^rview/', views.Rview.as_view()),
]