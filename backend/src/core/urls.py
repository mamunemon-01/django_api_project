from django.urls import include, path
from .views import PostListCreateView, PostRetrieveUpdateDestroyView, ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-details-update-delete'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-details-update-delete')
    # Define core app URLs here if needed in the future
]