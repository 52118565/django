from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 设置cookies
def cok(request):
    response = HttpResponse()
    response.set_cookie("name", "zs", max_age=3600*24)
    return response


# 获取cookie数据
def getcok(request):
    a = request.COOKIES.get("name")
    print(a)
    return HttpResponse("我是获取cookie")