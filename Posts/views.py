from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Post, Author, View, Subscribes
from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm, CommentForm, AddAuthor
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_result.html', context)
def get_author(user):
    qs = Author.objects.get(user=user)
    return qs

def index(request):
    if request.method == "POST":
        print("in here                   eeeeeeeeeeeeeeeeeeeeeee")
        email = request.POST["email"]
        new_signup = Subscribes()
        new_signup.user = request.user
        new_signup.email = email
        new_signup.save()

    queryset = Post.objects.all()[:3]
    latest_posts = Post.objects.order_by('-created_on')[:3]
    context = {
        'posts': queryset,
        'latest_posts': latest_posts
    }
    return render(request, "index.html", context)

def blog(request):
    categories = Post.objects.values('categories__title').annotate(Count('categories__title'))
    queryset = Post.objects.all()
    
    paginator = Paginator(queryset, 4)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(paginator.page_range[0])
    except EmptyPage:
        page_obj = paginator.page(paginator.page_range[0])
    
    latest_posts = Post.objects.order_by('-created_on')[:3]
    context = {
        'page_numbers': paginator.page_range,
        'categories': categories,
        'latest_posts': latest_posts,
        'queryset': page_obj
    }
    return render(request, "blog.html", context)


def post(request, id):
    latest_posts = Post.objects.order_by('-created_on')[:3]
    categories = Post.objects.values('categories__title').annotate(Count('categories__title'))
    post = get_object_or_404(Post, id=id)

    View.objects.get_or_create(
        post=post,
        user = get_author(request.user)
    )
    
    posts_id_list = []
    for dic in Post.objects.values('pk'):
        for i  in dic.values():
            posts_id_list.append(i)

    next_index = posts_id_list.index(id)+1
    prev_index = posts_id_list.index(id)-1
    
    if next_index == len(posts_id_list):
        next_post = ""
    else:
        next_post = Post.objects.get(pk=posts_id_list[next_index])
    
    if prev_index == -1:
        previous_post = ""
    else:
        previous_post = Post.objects.get(pk=posts_id_list[prev_index])
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        author = get_author(request.user)
        print(request.user)
        if form.is_valid():
            form.instance.author = author
            form.instance.post = post
            form.save()
            return redirect(reverse('post', kwargs={
                'id': post.pk
            }))


    context = {
        'post': post,
        'categories': categories,
        'latest_posts': latest_posts,
        'next_post': next_post,
        'previous_post': previous_post,
        'form': form

    }
    return render(request, "post.html", context)

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        author = get_author(request.user)
        print(form.errors)
        if form.is_valid():
            print('i am in valid')
            form.instance.author = author
            form.save()
            return redirect(reverse("blog"))
        return render(request, 'post-create.html', {'form': form})
        
        
    else:
        form = PostForm()
        return render(request, 'post-create.html', {'form': form})


def addauthor(request):
    form = AddAuthor()
    if request.method == "POST":
        form = AddAuthor(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect(reverse('blog'))
    context = {
        'form': form
    }
    return render(request, 'add_author.html', context)

