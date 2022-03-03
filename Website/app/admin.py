from django.contrib import admin
# Register your models here.
from .models import Article, ArticleTag, ArticleComment, ArticleCategory

admin.site.register(Article)
admin.site.register(ArticleCategory)
admin.site.register(ArticleTag)
admin.site.register(ArticleComment)