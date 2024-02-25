from django.contrib import admin
from .models import Content,UserInfo,Purpose

# Register your models here.
@admin.register(Content)
class Contentadmin(admin.ModelAdmin):
    list_display=['content']

@admin.register(UserInfo)
class userInfoadmin(admin.ModelAdmin):
   pass
@admin.register(Purpose)
class Purpose(admin.ModelAdmin):
   pass