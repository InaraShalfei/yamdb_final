from rest_framework import permissions
from .models import CustomUser


class IsYAMDBAdministrator(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == CustomUser.Role.ADMIN
