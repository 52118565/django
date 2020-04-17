from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View


def setses(request):
    request.session["name"] = "lisi"
    return HttpResponse("输入session值")


def getses(request):
    a = request.session.get("name")
    request.session.set_expiry(7)
    print(a)
    return HttpResponse("获取session")


def foo1(fun):
    def inner(request, *args, **kwargs):
        print("我是装饰器1")
        print(request.path)
        return fun(request, *args, **kwargs)
    return inner


def foo2(fun):
    def inner(request, *args, **kwargs):
        print("我是装饰器2")
        print(request.path)
        return fun(request, *args, **kwargs)
    return inner


class FoMixin1(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view()
        return foo1(view)


class FoMixin2(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view()
        return foo2(view)


# 类视图装饰器第三种方法
# @method_decorator(foo, name="dispatch")
class Rview(FoMixin1, FoMixin2, View):

    # 类视图装饰器第一种方法
    # @foo
    def get(self, request):
        print("我是GET方法")
        return HttpResponse("我只是GET方法")

    def post(self, request):
        print("我是POST方法")
        return  HttpResponse("我是POST方法")




