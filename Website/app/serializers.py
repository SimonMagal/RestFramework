from .models import Article, ArticleTag, ArticleComment, ArticleCategory
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Article
        fields = ["title", "slug", "text", 'category', 'owner',
                  'code', 'linenos', 'language', 'style']


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = ["name", "slug"]


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = ["name", "articles"]


class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = ["article", "text", "user"]


class UserSerializer(serializers.ModelSerializer):
    article = serializers.HyperlinkedRelatedField(many=True, view_name='article', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'article']
