from django.urls import path
from .views import get_blog, get_blog_detail, get_archieve

urlpatterns = [
    path('', get_blog, name = "get_blog"),
    path('<int:id>', get_blog_detail, name = "get_blog_detail"),
    path('<int:year>/<int:month>', get_archieve, name = "get_archieve")
]