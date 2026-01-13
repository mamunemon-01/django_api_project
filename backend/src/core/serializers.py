from rest_framework import serializers
from .models import User, Post, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'description', 'owner'
        ]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'price','quantity'
        ]