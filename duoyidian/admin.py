from django.contrib import admin

from duoyidian.models import DishClassifyInfo, DishInfo


class DishClassifyInfoAdmin(admin.ModelAdmin):
    list_display = ('classify', 'status', 'priority', 'create_at', 'update_at')


class DishInfoAdmin(admin.ModelAdmin):
    list_display = ('dish_classify', 'dish_name', 'dish_image', 'dish_price', 'status', 'priority', 'create_at', 'update_at')


admin.site.register(DishClassifyInfo, DishClassifyInfoAdmin)
admin.site.register(DishInfo, DishInfoAdmin)
