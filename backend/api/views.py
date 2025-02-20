from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from pics.models import Photo, Tag, Category, Comment
from .serializers import (
    PhotoListSerializer,
    PhotoCreateSerializer,
    TagSerializer,
    CategorySerializer,
    CommentSerializer
)
from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly


class PhotoViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с фотографиями."""
    permission_classes = (IsAuthorOrReadOnly,)
    
    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return PhotoCreateSerializer
        return PhotoListSerializer
    
    def get_queryset(self):
        return Photo.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с тегами."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с категориями."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с комментариями."""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        photo = get_object_or_404(Photo, id=self.kwargs.get('photo_id'))
        return photo.comments.all()

    def perform_create(self, serializer):
        photo = get_object_or_404(Photo, id=self.kwargs.get('photo_id'))
        serializer.save(author=self.request.user, photo=photo)
