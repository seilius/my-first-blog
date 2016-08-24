#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post

# Register your models here.
# 추가할 모델을 이곳에 기입 한다.
admin.site.register(Post)