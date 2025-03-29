from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm, PostForm
from blog.models import Post, Comment, Category
from django.http import HttpResponseRedirect
from blog.forms import CommentForm

# Create your views here.
def register(request):  
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

# User login view
def user_login(request):  # Ensure request is included
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("dashboard")  # Adjust redirect as needed
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

@login_required
def dashboard(request):
    return render(request, "blog/base.html")

# logout view
def logout(request):
    logout(request)
    messages.info(request, "Logged out")
    return redirect("login")

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Post added successfully!")
            return redirect('blog_index')
    else:
        form = PostForm()
    return render(request, "blog/add_post.html", {"form": form})

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

@login_required
def blog_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # Create the comment and associate the logged-in user as the author
            comment = form.save(commit=False)
            comment.author = request.user  # Assign the logged-in user as the author
            comment.post = post  # Associate the comment with the current post
            comment.save()  # Save the comment
            
            return redirect('blog:blog_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/blog_detail.html', {'post': post, 'form': form})

#def blog_detail(request, pk):
#    """Takes a primary key value, pk as an argument and retrieves the object with the given pk
#    The pk is the unique identifier of a database entry
#    Therefore a user is requesting for a unique post with a specific primary key that they provided"""
#    post = Post.objects.get(pk=pk)
#    form = CommentForm()
#    if request.method == "POST":
#        form = CommentForm(request.POST)
#        if form.is_valid():
#            comment = Comment(
#                author = form.cleaned_data["author"],
#                body = form.cleaned_data["body"],
#                post = post,
#            )
#            comment.save()
#            return HttpResponseRedirect(request.path_info)
#        
#    comments = Comment.objects.filter(post=post) #Queries the database for all the existing comments on a post
#    context = {
#        # creates context including the data for the post, filtered comments and the form
#        "post": post,
#        "comments": comments,
#        "form": CommentForm(),
#    }
#    return render(request, "blog/detail.html", context) # renders the detail.html with context