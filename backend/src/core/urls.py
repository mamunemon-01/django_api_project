from django.urls import include, path
from .views import PostListCreateRetrieveUpdateDestroyView 

urlpatterns = [
    path('posts/', PostListCreateRetrieveUpdateDestroyView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostListCreateRetrieveUpdateDestroyView.as_view(), name='post-detail-update-delete'),
    # Define core app URLs here if needed in the future
]