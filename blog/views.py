from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.
class PostListView(ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = 'blog/blog.html'
    context_object_name = 'Post'
    paginate_by = 10