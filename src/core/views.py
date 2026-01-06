from django.http import JsonResponse
from django.shortcuts import render

# third-party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from .serializers import PostSerializer
from .models import Post

# Create your views here.
class PostView(
    mixins.ListModelMixin,
    generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

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
