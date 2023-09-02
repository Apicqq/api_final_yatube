from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register(r'posts/(?P<post_id>\d+?)/comments',
                CommentViewSet, 'comments')
router.register('groups', GroupViewSet, 'groups')
router.register('posts', PostViewSet, 'posts')
router.register('follow', FollowViewSet, 'follows')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]
