from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from categories.models import Title
from users.models import CustomUser


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name='reviews', verbose_name='title',)
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="reviews"
    )
    text = models.TextField()
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='score'
    )
    pub_date = models.DateTimeField(
        "(Дата публикации отзыва", auto_now_add=True, db_index=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'review'
        verbose_name_plural = 'reviews'


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name='comments', verbose_name='review')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='author of comment')
    text = models.TextField()
    pub_date = models.DateTimeField(
        "Дата публикации комментария", auto_now_add=True, db_index=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
