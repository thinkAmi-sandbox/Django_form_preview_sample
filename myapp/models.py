from django.db import models

class Category(models.Model):
    name = models.CharField('category', max_length=255)
    
    # 表示した時に
    # Category object
    # のようになるのを防ぐため、__str__を定義
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('title', max_length=255)
    categories = models.ManyToManyField(Category)
    content = models.TextField('content')
    
