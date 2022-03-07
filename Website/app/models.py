from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from .permissions import IsOwnerOrReadOnly
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(ArticleCategory, related_name="category", on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)
    language = "python"
    linenos = False
    style = "friendly"
    code = "print(789)"

    def get_is_commented(self, user):
        return self.comments.filter(user=user).exist()

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

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



