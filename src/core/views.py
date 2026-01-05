from django.http import JsonResponse
from django.shortcuts import render

# third-party imports
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post

# Create your views here.

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        # data = {
        #     "country": "Venezuela",
        #     "message": "Donald Trump has President Maduro kidnapped!"
        # }
        qset = Post.objects.all()
        # serializer = PostSerializer(qset, many=True)
        data = qset.first()
        serializer = PostSerializer(data)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# def test_view(request):
#     data = {
#         "country": "Venezuela",
#         "message": "Donald Trump has President Maduro kidnapped!"
#     }

#     return JsonResponse(data)
