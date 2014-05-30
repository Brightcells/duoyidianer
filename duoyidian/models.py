# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext

from duoyidianer.basemodels import CreateUpdateMixin


import os
import time
import datetime


def upload_path(instance, old_filename):
    extension = os.path.splitext(old_filename)[1].lower()
    today = datetime.datetime.today()
    timestamp = str(time.time())
    file_path = 'duodyidianer/image/{year}{month}/{timestamp}{extension}'.format(
        year=today.year,
        month=today.month,
        timestamp=timestamp,
        extension=extension)
    return file_path


# 菜谱分类信息表
class DishClassifyInfo(CreateUpdateMixin):
    classify = models.CharField(_(u'classify'), max_length=255, blank=True, null=True, help_text=u'菜谱分类')
    status = models.BooleanField(default=True)
    priority = models.IntegerField(blank=True, null=True, help_text=u'优先级')

    class Meta:
        verbose_name = _(u'dishclassifyinfo')
        verbose_name_plural = _(u'dishclassifyinfo')

    def __unicode__(self):
        return unicode(self.classify)

    def _data(self):
        return {
            'pk': self.pk,
            'classify': self.classify,
        }

    data = property(_data)


# 菜品信息表
class DishInfo(CreateUpdateMixin):
    dish_classify = models.ForeignKey(DishClassifyInfo, blank=True, null=True, help_text=u'所属菜谱分类')
    dish_name = models.CharField(_(u'dish_name'), max_length=255, blank=True, null=True, help_text=u'菜名')
    dish_image = models.ImageField(_('dish_image'), upload_to=upload_path, blank=True, null=True, help_text=u'菜品配图')
    dish_price = models.IntegerField(blank=True, null=True, help_text=u'菜品价钱')
    status = models.BooleanField(default=True)
    priority = models.IntegerField(blank=True, null=True, help_text=u'优先级')

    class Meta:
        verbose_name = _(u'dishinfo')
        verbose_name_plural = _(u'dishinfo')

    def __unicode__(self):
        return unicode(self.dish_name)

    def _data(self):
        return {
            'pk': self.pk,
            'name': self.dish_name,
            'image': self.dish_image.url if self.dish_image else '',
            'price': self.dish_price
        }

    data = property(_data)
