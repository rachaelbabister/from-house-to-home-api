from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Represents a category within an application.
    """
    name = models.CharField(max_length=64, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name