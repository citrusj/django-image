from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Content(models.Model):
    title=models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField(default='')

    image = models.ImageField(upload_to='images/',blank=True)


    file = models.FileField(upload_to='documents/%Y.%m',blank=True) #파일 저장 위치가 document/(년.월)폴더 로 설정됨.