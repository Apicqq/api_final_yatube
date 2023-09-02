from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .permissions import PermissionMixin
from .serializers import (CommentSerializer,
                          GroupSerializer,
                          FollowSerializer,
                          PostSerializer)
from posts.models import Follow, Group, Post, User


class PostViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(PermissionMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(PermissionMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    @property
    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    @property
    def get_user(self):
        return get_object_or_404(User, username=self.request.user)

    def get_queryset(self):
        return self.get_user.following.all()

    def perform_create(self, serializer):
        serializer.save(user=self.get_user)
