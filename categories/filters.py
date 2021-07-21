import django_filters

from .models import Category, Genre, Title


class TitleFilter(django_filters.FilterSet):
    genre = django_filters.filters.ModelMultipleChoiceFilter(
        queryset=Genre.objects.all(),
        field_name='genre__slug',
        to_field_name='slug',
    )
    category = django_filters.filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        field_name='category',
        to_field_name='slug',
    )
    name = django_filters.CharFilter(lookup_expr='contains')
    year = django_filters.NumberFilter()

    class Meta:
        model = Title
        fields = ['category', 'genre', 'name', 'year']
