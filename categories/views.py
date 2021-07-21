from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, permissions, viewsets

from categories.models import Category, Genre, Title
from categories.serializers import (CategorySerializer, GenreSerializer,
                                    TitleWriteSerializer, TitleReadSerializer)

from .filters import TitleFilter
from .paginator import StandardPagination
from .permissions import IsStaffOrReadOnly


class ViewSet(mixins.CreateModelMixin,
              mixins.ListModelMixin,
              mixins.DestroyModelMixin,
              viewsets.GenericViewSet):
    pass


class CategoryViewSet(ViewSet):
    lookup_field = 'slug'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    pagination_class = StandardPagination
    permission_classes = [IsStaffOrReadOnly]


class GenreViewSet(ViewSet):
    lookup_field = 'slug'
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    pagination_class = StandardPagination
    permission_classes = [IsStaffOrReadOnly]


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(
        rating=Avg('reviews__score')).order_by('id', )
    serializer_class = TitleWriteSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return TitleReadSerializer
        return TitleWriteSerializer
