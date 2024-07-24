from rest_framework import generics
from django.http import Http404
from .models import Profile
from .serializers import ProfileSerializer
from home_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListCreateAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
    
class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you are the owner.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()