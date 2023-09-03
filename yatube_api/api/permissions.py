from rest_framework import permissions


class AuthorizedPermission(permissions.BasePermission):
    message = 'Редактирование чужого контента запрещено.'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class AuthenticatedPermission(permissions.BasePermission):
    message = ('Неаутентифицированным пользователям контент'
               'недоступен.')

    def has_permission(self, request, view):
        return request.user.is_authenticated

# Я понимаю, что это костыль, но без него не срастается. Во вьюсете
# Фоллоу прописан кверисет через request.user, если этот пермишен не вводить,
# то тест падает с ошибкой, что у AnonymousUser нет метода following
