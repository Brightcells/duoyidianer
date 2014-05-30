# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext

from duoyidianer.basemodels import CreateUpdateMixin


# 用户注册信息表
class UserInfo(CreateUpdateMixin):
    username = models.CharField(_(u'username'), max_length=255, blank=True, null=True, help_text=u'用户名称')
    password = models.CharField(_(u'password'), max_length=255, blank=True, null=True, help_text=u'用户密码')
    email = models.EmailField(_(u'email'), max_length=255, blank=True, null=True, help_text=u'用户邮箱')

    class Meta:
        verbose_name = _(u'userinfo')
        verbose_name_plural = _(u'userinfo')

    def __unicode__(self):
        return unicode(self.username)
