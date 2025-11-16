from django.urls import path
from .views import (
    PostListView, PostDetailView,
    CommentListView, CommentDetailView,
    CategoryListView
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
