from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from home_api.permissions import IsOwnerOrReadOnly
from .models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer


class CategoryList(generics.ListAPIView):
    """
    API view to list all categories.
    Allows filtering by name.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a category by id.
    Only the owner can update or delete.
    """
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
