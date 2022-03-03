from django.urls import path, include
from rest_framework import routers, viewsets
from . import views

# Routers provide an easy way of automatically determining the URL conf.
"""
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
"""


urlpatterns = [
    path('article/<int:pk>', views.ArticleView.as_view(), name='ArticleView'),
    path('article_comment/', views.ArticleCommentView.as_view(), name='ArticleCommentView5'),
    path('article_tag/<int:pk>', views.ArticleTagView.as_view(), name='ArticleTagView'),
    path('article_category/<int:pk>', views.ArticleCategoryView.as_view(), name='ArticleCategoryView'),
]

"""
urlpatterns = [
    path('', include(routers.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('post_item/', views.getdata, name='getdata' ),
]"""