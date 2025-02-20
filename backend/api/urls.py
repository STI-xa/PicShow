from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PhotoViewSet,
    TagViewSet,
    CategoryViewSet,
    CommentViewSet,
)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('photos', PhotoViewSet, basename='photos')
router_v1.register('tags', TagViewSet, basename='tags')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register(
    r'photos/(?P<photo_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
