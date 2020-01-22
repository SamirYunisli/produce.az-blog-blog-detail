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

    first_count = Post.objects.filter(test_date__year = 2020, test_date__month = 1).count()
    second_count = Post.objects.filter(test_date__year = 2019, test_date__month = 11).count()
    third_count = Post.objects.filter(test_date__year = 2019, test_date__month = 12).count()


    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'posts': posts,
        'first_count': first_count,
        'second_count': second_count,
        'third_count': third_count,
    }
    return render(request, 'blog.html', context)


def get_blog_detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post
    }
    return render(request, 'blog-detail.html', context)

def get_archieve(request, year, month):
    post_list = Post.objects.filter(test_date__year = year, test_date__month = month)

    if request.method == 'POST':
        search = request.POST.get('search')
        post_list = Post.objects.filter(Q(title__icontains=search) | Q(text__icontains=search) | Q(description__icontains=search))
    
    first_count = Post.objects.filter(test_date__year = 2020, test_date__month = 1).count()
    second_count = Post.objects.filter(test_date__year = 2019, test_date__month = 11).count()
    third_count = Post.objects.filter(test_date__year = 2019, test_date__month = 12).count()

    paginator = Paginator(post_list, 2)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'posts': posts,
        'first_count': first_count,
        'second_count': second_count,
        'third_count': third_count,
    }
    return render(request, 'blog.html', context)