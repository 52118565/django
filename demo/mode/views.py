from django.shortcuts import render
from ses.models import BookInfo, HeroInfo
from django.http import HttpResponse
from django.views import View
from datetime import date
from django.db.models import F, Q, Sum, Avg, Max, Min

# Create your views here.

# class Mode(View):
#     def get(self, request):
#         book = BookInfo(
#             btitle="西游记",
#             bpub_date=date(1988,10,10),
#             bread=100,
#             bcomment=1000
#         )
#         book.save()
#         return HttpResponse("save添加数据")


# class Mode(View):
#     def get(self, request):
#         HeroInfo.objects.create(
#             hname="孙悟空",
#             hgender=0,
#             hbook=BookInfo.objects.get(id=5)
#         )
#         hero = HeroInfo(
#             hname="沙悟净",
#             hgender=0,
#             hbook=BookInfo.objects.get(id=5)
#         )
#
#         hero.save()
#         return HttpResponse("添加数据")


class Mode(View):
    def get(self, request):
        a = HeroInfo.objects.all()
        print(a)
        b = BookInfo.objects.get(pk=5)
        print(b, type(b))
        print(b.bcomment)
        c = HeroInfo.objects.count()
        print(c)

        d = BookInfo.objects.filter(btitle__contains="记")
        print(d)

        e = HeroInfo.objects.filter(hcomment__isnull=True)
        print(e)

        f = BookInfo.objects.exclude(pk__in=[2, 3, 4])
        print(f)

        g = HeroInfo.objects.filter(id__lte=5)
        print(g)

        # HeroInfo.objects.get(id=18).delete()

        return HttpResponse("查询数据")


# class Sel(View):
#     def get(self, request):
#         hero = HeroInfo.objects.get(hname="沙悟净")
#         hero.hname = "悟净"
#         hero.save()
#         return HttpResponse("修改数据")


# class Sel(View):
#     def get(self, request):
        # hero = HeroInfo(
        #     id=18,
        #     hname="猪悟能",
        #     hgender=0,
        #     hbook=BookInfo.objects.get(id=5)
        # )
        # hero.save()

        # HeroInfo.objects.filter(hname="猪悟能").update(hname="猪八戒")
        #
        # return HttpResponse("修改数据")


# class Sel(View):
#     def get(self, request):
#         a = BookInfo.objects.filter(bread__lte=F("bcomment"))
#         print(a)
#
#         b = BookInfo.objects.filter(bread__lte=100, id__gte=1)
#         print(b)
#
#         c = HeroInfo.objects.filter(Q(hbook__lte=2) | Q(hgender=0))
#         print(c)
#
#         d = BookInfo.objects.filter(~Q(id=3))
#         print(d)
#
#         f = BookInfo.objects.aggregate(Sum('bread'))
#         g = BookInfo.objects.aggregate(Avg('bcomment'))
#         h = BookInfo.objects.aggregate(Max('bpub_date'))
#
#         i = BookInfo.objects.all().order_by("bpub_date")
#
#         print(f)
#         print(g)
#         print(h)
#         print(i)
#
#         return HttpResponse("对比数据")


class Sel(View):
    def get(self, request):
        hero = HeroInfo.objects.get(id=1)
        a = hero.hbook
        a = a.bread
        print(a)

        b = BookInfo.objects.get(btitle="西游记")
        c = b.heroinfo_set.filter(id=19)
        print(c)

        d = BookInfo.objects.filter(heroinfo__hname__contains="空")
        print(d)

        e = HeroInfo.objects.filter(hbook__bcomment__lte=1000)
        print(e)

        return HttpResponse("关联查询")