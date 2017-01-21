from django.db import models
from djangotoolbox.fields import ListField, DictField
# Create your models here.


from django.db import models

class Article(models.Model):
    article_id = models.CharField(max_length=50)
    content = models.TextField()
    user_name =models.CharField(max_length=50)
    user_image=models.TextField()
    comments=DictField()

class Image(models.Model):
    article_id = models.CharField(max_length=50)
    content = models.TextField()
    user_name =models.CharField(max_length=50)
    user_image=models.TextField()
    content_image=models.TextField()
    comments=DictField()
    class Meta:
        ordering = ["-article_id"]