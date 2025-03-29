# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    # Post class
    title = models.CharField(max_length=225)
    categories = models.ManyToManyField("Category", related_name="posts")
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


#class Post(models.Model):
#    """Post class"""
#    title = models.CharField(max_length=225)
#    categories = models.ManyToManyField("Category", related_name="posts")
#    body = models.TextField()
#    author = models.ForeignKey(User, on_delete=models.CASCADE)
#    created_on = models.DateTimeField(auto_now_add=True)
#    last_modified = models.DateTimeField(auto_now=True)
#
#    def __str__(self):
#        return self.title

class Category(models.Model):
    """Category model class"""
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
