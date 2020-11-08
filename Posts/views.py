from django.shortcuts import render, get_object_or_404
from .models import Post
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    queryset = Post.objects.all()[:3]
    context = {
        'posts': queryset
    }
    return render(request, "index.html", context)

def blog(request):
    categories = Post.objects.values('categories__title').annotate(Count('categories__title'))
    queryset = Post.objects.all()
    
    paginator = Paginator(queryset, 1)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(paginator.page_range[0])
    except EmptyPage:
        page_obj = paginator.page(paginator.page_range[0])
    
    latest_posts = Post.objects.order_by('-created_on')
    context = {
        'page_numbers': paginator.page_range,
        'categories': categories,
        'latest_posts': latest_posts,
        'queryset': page_obj
    }
    return render(request, "blog.html", context)

def post(request, id):
    latest_posts = Post.objects.order_by('-created_on')
    categories = Post.objects.values('categories__title').annotate(Count('categories__title'))
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
        'categories': categories,
        'latest_posts': latest_posts,

    }
    return render(request, "post.html", context)

