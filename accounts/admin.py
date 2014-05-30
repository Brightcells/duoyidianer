from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from accounts.models import UserInfo


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'create_at', 'update_at')


admin.site.register(UserInfo, UserInfoAdmin)
