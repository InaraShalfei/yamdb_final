from django.contrib import admin

from .models import Category, Genre, Title


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'description', 'category')
    search_fields = ('name', 'year', 'genre', 'category')
    list_filter = ('year',)
    empty_value_display = '-пусто-'
