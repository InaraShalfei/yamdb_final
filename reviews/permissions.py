from rest_framework import permissions

from users.models import CustomUser


class IsAuthorModerAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.role == CustomUser.Role.MODERATOR
                or request.user.role == CustomUser.Role.ADMIN):
            return True
