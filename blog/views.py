from django.shortcuts import render
from blog.models import Post, Comment
from django.http import HttpResponseRedirect
from blog.forms import CommentForm


# Create your views here.

def blog_index(request):
    posts = Post.objects.all().order_by("created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        # This is a query set filter. Tell the backend service on what to do
        # It will only pick the selected categories
        categories__name__contains=category
    ).order_by("-created_on") # orders posts starting with the most recent one

    # add the posts to the category context
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    """Takes a primary key value, pk as an argument and retrieves the object with the given pk
    The pk is the unique identifier of a database entry
    Therefore a user is requesting for a unique post with a specific primary key that they provided"""
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        
    comments = Comment.objects.filter(post=post) #Queries the database for all the existing comments on a post
    context = {
        # creates context including the data for the post, filtered comments and the form
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "blog/detail.html", context) # renders the detail.html with context