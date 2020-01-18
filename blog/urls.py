from django.urls import path
from .views import get_blog, get_blog_detail

urlpatterns = [
    path('', get_blog, name = "get_blog"),
    path('<int:id>', get_blog_detail, name = "get_blog_detail")
]