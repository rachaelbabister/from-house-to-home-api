from rest_framework import generics, permissions
from home_api.permissions import IsOwnerOrReadOnly
from followers.models import Follower
from followers.serializers import FollowerSerializer
from posts.models import Post
from posts.serializers import PostSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    List or create follower relationships when logged in.
    """
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower.
    'Destroy' a follower, i.e. unfollow someone if owner
    """
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]


class FollowedPosts(generics.ListAPIView):
    """
    Show posts from followed users.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_users = Follower.objects.filter(
            owner=user).values_list('followed', flat=True)
        return Post.objects.filter(
                owner__in=followed_users).order_by('-created_on')