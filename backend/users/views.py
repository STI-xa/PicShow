from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from .models import User
from api.serializers import CustomUserSerializer, CustomUserCreateSerializer
from api.permissions import IsAdminOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с пользователями."""
    queryset = User.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserCreateSerializer
        return CustomUserSerializer

    def perform_create(self, serializer):
        serializer.save()
