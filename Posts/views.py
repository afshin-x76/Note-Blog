from django.shortcuts import render
from .models import Post

def index(request):
    queryset = Post.objects.all()[:3]
    context = {
        'posts': queryset
    }
    return render(request, "index.html", context)

def blog(request):
    return render(request, "blog.html")

def post(request):
    return render(request, "post.html")

