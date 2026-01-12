from django.http import JsonResponse
from django.shortcuts import render

# third-party imports
# from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from .serializers import PostSerializer
from .models import Post

# Create your views here.
# class PostView(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     def get(self, request, *args, **kwargs):
#         return self.list(self, request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    

# class PostCreateView(
#     mixins.ListModelMixin,
#     generics.CreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.list(self, request, *args, **kwargs)

class PostListCreateView(generics.ListCreateAPIView):
    # lookup_field = 'pk' # to use primary key instead of id for lookup with parameter
    # pagination_class = LimitOffsetPagination # to enable pagination
    serializer_class = PostSerializer # to specify serializer
    # def get_serializer_class(self):# to dynamically set serializer class
    #     return PostSerializer
    queryset = Post.objects.all() # to specify queryset for all posts

    # to dynamically set queryset
    # def get_queryset(self):
    #     querset = Post.objects.all()
    #     if self.request.user.is_authenticated:
    #         # get filetered queryset for logged in user
    #         querset = querset.filter(owner=self.request.user)
    #     else:
    #         querset = Post.objects.none()

    #     return querset
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # lookup_field = 'pk' # to use primary key instead of id for lookup with parameter
    serializer_class = PostSerializer # to specify serializer
    queryset = Post.objects.all() # to specify queryset for all posts

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# class TestView(APIView):
#     permission_classes = (IsAuthenticated, )
#     def get(self, request, *args, **kwargs):
#         # data = {
#         #     "country": "Venezuela",
#         #     "message": "Donald Trump has President Maduro kidnapped!"
#         # }
#         qset = Post.objects.all()
#         # serializer = PostSerializer(qset, many=True)
#         data = qset.first()
#         serializer = PostSerializer(data)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# def test_view(request):
#     data = {
#         "country": "Venezuela",
#         "message": "Donald Trump has President Maduro kidnapped!"
#     }

#     return JsonResponse(data)
