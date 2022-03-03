from .serializers import ArticleSerializer, ArticleCategorySerializer, ArticleTagSerializer, ArticleCommentSerializer
from app.models import Article, ArticleCategory, ArticleTag, ArticleComment
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins


"""
class ArticleView(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class ArticleCategoryView(APIView):
    def get_object(self, pk):
        try:
            return ArticleCategory.objects.get(pk)
        except ArticleCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = ArticleCategorySerializer(category)
        return Response(serializer.data)


class ArticleTagView(APIView):
    def get_object(self, pk):
        try:
            return ArticleTag.objects.get(pk)
        except ArticleTag.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = ArticleTagSerializer(tag)
        return Response(serializer.data)


class ArticleCommentView(APIView):t
    def get_object(self, pk):
        try:
            return ArticleComment.objects.get(pk)
        except ArticleComment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = ArticleCommentSerializer(comment)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = ArticleCommentSerializer(comment)
"""



class ArticleView(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArticleCategoryView(mixins.RetrieveModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArticleTagView(mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = ArticleTag.objects.all()
    serializer_class = ArticleTagSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArticleCommentView(mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = ArticleComment.objects.all()
    serializer_class = ArticleCommentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)
