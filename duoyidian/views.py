from django.shortcuts import render

from duoyidian.models import DishClassifyInfo, DishInfo


def home(request, cid=-1):
    if cid == -1:
        try:
            cid = DishClassifyInfo.objects.filter(status=True).order_by('priority').values('pk')[0]['pk']
        except:
            cid = -1

    menus = DishClassifyInfo.objects.filter(status=True).order_by('priority')
    menus = [menu.data for menu in menus]

    dishs = DishInfo.objects.filter(status=True, dish_classify__pk=cid).order_by('priority')
    dishs = [dish.data for dish in dishs]

    return render(
        request,
        'duoyidian/home.html',
        dict(menus=menus, dishs=dishs)
    )
