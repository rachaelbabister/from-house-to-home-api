from rest_framework import generics, permissions, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from home_api.permissions import IsOwnerOrReadOnly
from .models import Post, Category
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List posts or creates a post if logged in.
    """
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_on')

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_on',
    ]
    search_fields = [
        'owner__username',
        'title',
        'content',
        'category_name',
    ]
    filterset_fields = [
        # user feed
        'owner__followed__owner__profile',
        # user liked posts
        'likes__owner__profile',
        # user posts
        'owner__profile',
        # categories
        'category',
    ]

    def perform_create(self, serializer):
        """
        Creates new post
        """
        category_name = self.request.data.get('category', None)
        if category_name:
            category = Category.objects.get(name=category_name)
            serializer.save(owner=self.request.user, category=category)
        else:
            serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_on')
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
