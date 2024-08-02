from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model
    """
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_on']


class CategoryDetailSerializer(CategorySerializer):
    """
    Serializer for the Comment model used in Detail view
    """
    category_id = serializers.ReadOnlyField(source='id')

    class Meta:
        model = Category
        fields = ['id', 'name', 'created_on', 'category_id']
