# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 Qimin Huang <kimi.huang@brightcells.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from django.shortcuts import render

from duoyidian.models import DishClassifyInfo, DishInfo

from utils.utils import getUsr


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
        dict(menus=menus, dishs=dishs, usr=getUsr(request))
    )
