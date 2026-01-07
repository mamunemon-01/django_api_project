from django.urls import include, path
from .views import PostListCreateView 

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    # Define core app URLs here if needed in the future
]