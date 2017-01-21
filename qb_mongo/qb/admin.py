from django.contrib import admin

# Register your models here.
from qb.models import *

class ArticleAdmin(admin.ModelAdmin):
     list_display = ('article_id', 'content')
admin.site.register(Article,ArticleAdmin)

admin.site.register(Image)