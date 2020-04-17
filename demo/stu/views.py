from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.


def request1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')

    print(a)
    print(b)
    print(alist)
    return HttpResponse("我是接受请求方式1")


def request2(request, city, year):
    print(city)
    print(year)
    return HttpResponse("我是接受请求方式2")


def request3(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')

    print(a)
    print(b)
    print(alist)
    return HttpResponse("我是POST请求方式")


def request4(request):
    value = json.loads(request.body.decode())
    a = value["a"]
    b = value["b"]

    print(value)
    print(a)
    print(b)
    return HttpResponse("我是Json请求方式")