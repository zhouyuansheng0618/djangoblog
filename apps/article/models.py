from django.db import models


# Create your models here.

class ArticleModel(models.Model):
    title = models.CharField(max_length=128, verbose_name='文章名称')
    title = models.CharField(max_length=128, verbose_name='文章名称')
