from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models


class Category(models.Model):
    name = models.TextField(max_length=100, verbose_name='name')
    slug = models.SlugField(max_length=100, verbose_name='slug', unique=True)

    class Meta:
        ordering = ('slug',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        constraints = [
            models.UniqueConstraint(
                fields=['slug'],
                name='unique_slug'
            )
        ]

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('slug',)
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.TextField(max_length=100, verbose_name='name')
    year = models.PositiveIntegerField(verbose_name='year',
                                       validators=[MaxValueValidator(
                                           datetime.now().year)])
    description = models.TextField(max_length=200, verbose_name='description')
    genre = models.ManyToManyField(Genre, related_name='titles',
                                   verbose_name='genre')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 verbose_name='category',
                                 null=True,
                                 related_name='titles')

    class Meta:
        ordering = ('genre__slug',)
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'

    def __str__(self):
        return self.name
