from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin view for Category.
    Displays 'id', 'name', and 'created_on'.
    Allows searching by 'name'.
    Shows 20 items per page.
    """
    list_display = ('id', 'name', 'created_on')
    search_fields = ('name',)
    list_per_page = (20)