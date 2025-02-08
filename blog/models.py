# models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """Post class"""
    title = models.CharField(max_length=225)
    categories = models.ManyToManyField("Category", related_name="posts")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    """Category model class"""
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Comment(models.Model):
    """Comments class"""
    author = User()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"