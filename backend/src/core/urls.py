from django.urls import include, path
from .views import PostListCreateView, PostRetrieveUpdateDestroyView 

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail-update-delete'),
    # Define core app URLs here if needed in the future
]