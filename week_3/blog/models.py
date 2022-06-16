from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    
class Article(models.Model):
    article_user = models.CharField("글 작성자", max_length=20, unique=True)
    article_title = models.CharField("글 제목", max_length=128)
    article_desc = models.CharField("글 내용", max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    