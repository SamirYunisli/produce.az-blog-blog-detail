from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
from django.db.models import Q
# Create your views here.

def get_blog(request):
    post_list = Post.objects.all()

    if request.method == 'POST':
        search = request.POST.get('search')
        post_list = Post.objects.filter(Q(title__icontains=search) | Q(text__icontains=search) | Q(description__icontains=search))

    paginator = Paginator(post_list, 2)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'posts': posts
    }
    return render(request, 'blog.html', context)


def get_blog_detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post
    }
    return render(request, 'blog-detail.html', context)