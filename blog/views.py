from django.shortcuts import render
from rest_framework.views import APIView
from .models import BlogPost
from rest_framework.response import Response

# Create your views here.
class BlogView(APIView):
    def get(self, request):
        blog_data= BlogPost.objects.all().values()
        return Response({"data":blog_data})

    def post(self,request):
        data = request.data
        BlogPost.objects.create(
            blog_title = data["blog_title"],
            blog_description= data["blog_description"],
            blog_content = data["blog_content"],
            author=data["author"]

        )
