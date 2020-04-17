from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def setses(request):
    request.session["name"] = "lisi"
    return HttpResponse("输入session值")


def getses(request):
    a = request.session.get("name")
    request.session.set_expiry(7)
    print(a)
    return HttpResponse("获取session")