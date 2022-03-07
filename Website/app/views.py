from .serializers import ArticleSerializer, ArticleCategorySerializer, ArticleTagSerializer, ArticleCommentSerializer, UserSerializer
from app.models import Article, ArticleCategory, ArticleTag, ArticleComment
from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers, viewsets

class ArticleView(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


"""
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        article = self.get_object()
        return Response(article.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
"""


class ArticleListView(mixins.ListModelMixin,
                      generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ArticleCategoryView(mixins.RetrieveModelMixin,
                          mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          generics.GenericAPIView):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArticleTagView(mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     generics.GenericAPIView):
    queryset = ArticleTag.objects.all()
    serializer_class = ArticleTagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArticleCommentView(mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         generics.GenericAPIView):
    queryset = ArticleComment.objects.all()
    serializer_class = ArticleCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, format=format)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)




class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('app.user-list', request=request, format=format),
        'article': reverse('app.article', request=request, format=format)
    })


class ArticleHighlight(generics.GenericAPIView):
    queryset = Article.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        article = self.get_object()
        return Response(article.highlighted)


