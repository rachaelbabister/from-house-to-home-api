from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.LikeList.as_view()),
    path('likes/<int:pk>/', views.LikeDetail.as_view()),
    path('liked-posts/', views.LikedPosts.as_view(), name='liked-posts'),
]