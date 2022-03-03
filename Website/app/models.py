from django.db import models
import django
from django.contrib.auth.models import User
# Create your models here.


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(ArticleCategory, related_name="category", on_delete=models.CASCADE)


    def get_is_commented(self, user):
        return self.comments.filter(user=user).exist()



    def __str__(self) -> str:
        return str(self.title)



class ArticleTag(models.Model):
    name = models.CharField(max_length=255)
    articles = models.ManyToManyField(Article)

    def __str__(self):
        return self.name


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

