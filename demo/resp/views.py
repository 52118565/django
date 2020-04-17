from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse



# Create your views here.

# 添加响应头键值
def resp(request):
    response = HttpResponse("我是字符串，但我的类型会显示Json", content_type="application/json", status="299")
    response["insert"] = "我是增加的"
    return response


# 输出字典，响应返回Json
def js(request):
    mydict = {'name': 'zs', 'age': 20}
    return JsonResponse(mydict)


# 输出字符串，响应返回类型还是Json
def js2(request):
    a = "hahaha"
    return JsonResponse(a, safe=False)


# 跳转页面
def tiao(request):
    a = reverse("a:j")
    return redirect(a)