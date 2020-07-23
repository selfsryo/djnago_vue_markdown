from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


def index(request):
	posts = Post.objects.all()
	return render(request, 'app/index.html', {'posts': posts})


class PostList(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
