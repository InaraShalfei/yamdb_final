from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin'
        MODERATOR = 'moderator'
        USER = 'user'

    email = models.EmailField(unique=True, verbose_name='email')
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=20, choices=Role.choices,
                            verbose_name='role', default=Role.USER)
    confirmation_code = models.CharField(max_length=100,
                                         verbose_name='confirmation_code')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email
