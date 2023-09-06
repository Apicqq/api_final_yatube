from django.urls import include, path
from rest_framework import routers

from api.views import (CommentViewSet,
                       GroupViewSet,
                       PostViewSet,
                       FollowViewSet,
                       UserViewSet)

yatube_router_v1 = routers.DefaultRouter()
yatube_router_v1.register(r'posts/(?P<post_id>\d+?)/comments',
                          CommentViewSet, 'comments')
yatube_router_v1.register('groups', GroupViewSet, 'groups')
yatube_router_v1.register('posts', PostViewSet, 'posts')
yatube_router_v1.register('follow', FollowViewSet, 'follows')
yatube_router_v1.register('users', UserViewSet, 'users')

urlpatterns = [
    path('v1/', include(yatube_router_v1.urls)),
    path('v1', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]
