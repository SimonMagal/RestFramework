from django.urls import path, include
from rest_framework import routers, viewsets
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
# Routers provide an easy way of automatically determining the URL conf.
"""
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
"""


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('article/<int:pk>', views.ArticleView.as_view(), name='ArticleView'),
    path('article_comment/', views.ArticleCommentView.as_view(), name='ArticleCommentView'),
    path('article_tag/<int:pk>', views.ArticleTagView.as_view(), name='ArticleTagView'),
    path('article_category/<int:pk>', views.ArticleCategoryView.as_view(), name='ArticleCategoryView'),
    path('article_list/', views.ArticleListView.as_view(), name='ArticleList'),
    path('users/', views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='article'),
    path('article/<int:pk>/highlight/', views.ArticleHighlight.as_view(), name="ArticleHighlight"),
    ])



"""
urlpatterns = [
    path('', include(routers.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('post_item/', views.getdata, name='getdata' ),
]"""