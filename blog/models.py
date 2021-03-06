import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone


STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)


def lnglat_validator(value):    
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):        
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    title = models.CharField(max_length = 100, verbose_name = '제목', help_text='포스팅 제목을 입력해주세요. 100자 내외.') # 길이 제한이 있는 문자열
    content = models.TextField(verbose_name = '내용')              # 길이 제한이 없는 문자열
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
        validators=[lnglat_validator],
        help_text='경도, 위도 포맷으로 입력')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-id']
    



