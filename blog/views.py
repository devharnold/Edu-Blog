from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm, PostForm, BlogForm
from blog.models import Post, Comment, Category
from django.http import HttpResponseRedirect, HttpResponseForbidden
from blog.forms import CommentForm
from .models import Post

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
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("home")  # Redirects to home after login
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

def home(request):
    posts = Post.objects.all().order_by("-created_on")  # Get all posts, newest first
    form = BlogForm()  # Load empty form for modal
    return render(request, "blog/home.html", {"posts": posts, "form": form})

@login_required
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()  # Save the post
            form.save_m2m()  # Save the many-to-many relationships (categories)
            return redirect('home')  # Redirect after saving
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})


# @login_required
# def dashboard(request):
#     return render(request, "blog/base.html")

@login_required
def dashboard(request):
    user_posts = Post.objects.filter(author=request.user)  # Get only user's blogs
    return render(request, "dashboard.html", {"user_posts": user_posts})

# logout view
def logout_view(request):
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
def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all() # This retrieves all
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create the comment and associate the logged-in user as the author
            comment = comment_form.save(commit=False)
            comment.author = request.user  # Assign the logged-in user as the author
            comment.post = post  # Associate the comment with the current post
            comment.save()  # Save the comment
            
            return redirect('blog:blog_detail', pk=pk)
    else:
        form = CommentForm()

    #return render(request, 'blog/blog_detail.html', {'post': post, 'form': form})
    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })

def category_posts(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = category.posts.all()
    return render(request, "blog/category_posts.html", {"category": category, "posts": posts})

@login_required
def edit_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return HttpResponseForbidden("You can't edit this blog.")
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = PostForm(instance=post)

    return render(request, "edit_blog.html", {"form": form})

@login_required
def delete_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return HttpResponseForbidden("You can't delete this blog.")

    if request.method == "POST":
        post.delete()
        return redirect("dashboard")

    return render(request, "confirm_delete.html", {"post": post})

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            # Ensure the categories are valid
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()  # Save the post to get its ID
            form.save_m2m()  # This will save the many-to-many relationships like categories

            return redirect('blog_home')  # Redirect to the home page or the detail page
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})

#def create_blog(request):
#    if request.method == 'POST':
#        form = BlogForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user  # Assuming the post author is the logged-in user
#            post.save()
#            form.save_m2m()  # Save the many-to-many relationships (categories)
#            return redirect('blog_home')  # Redirect to the blog homepage after saving
#    else:
#        form = BlogForm()
#
#    return render(request, 'create_blog.html', {'form': form})

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