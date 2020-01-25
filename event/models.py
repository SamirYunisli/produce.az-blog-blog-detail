from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255, null = True)
    description = models.CharField(max_length=255, null = True, blank = True)
    text = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'blog_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(null = True, blank = True)
    end_date = models.DateField(null = True, blank = True)
    test_date = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.title or self.id
