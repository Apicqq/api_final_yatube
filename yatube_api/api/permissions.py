from rest_framework import permissions


class AuthorizedPermission(permissions.BasePermission):
    message = 'Редактирование чужого контента запрещено.'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class ReadOnlyPermission(permissions.BasePermission):
    message = ('Неаутентифицированным пользователям контент'
               'доступен только для чтения.')

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class PermissionMixin:
    def get_permissions(self):
        return ((ReadOnlyPermission(),) if self.action in ('retrieve', 'list')
                else super().get_permissions())
