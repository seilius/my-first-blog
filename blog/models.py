#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

'''
author foreingkey reference auth.User
title char(200)text largeText
create_date DateTime
published_date DateTime Not Null
'''

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True, null=True)

    # 수정시간 기록 함수
    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    # 테이블 명 표출 메서드(기본)
    def __str__(self):
        return self.title