from django.urls import path
from . import views
from .views import register, user_login, logout_view, dashboard, blog_detail, home, create_blog, category_posts

urlpatterns = [
    path("", home, name="home"),  # Home page
    path("create/", views.create_blog, name="create_blog"),  # Add blog post
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),  # Blog detail page
    path("category/<str:category>/", views.blog_category, name="blog_category"),  # Categories
    path("category/<str:category_name>/", views.category_posts, name="category_posts"),
    path("register/", views.register, name="register"),  # Register
    path("login/", user_login, name="login"),  # Login
    path("logout/", logout_view, name="logout"),  # Logout
    path("dashboard/", views.dashboard, name="dashboard"),  # Dashboard
    path("blogs/", views.blog_index, name="blog_index"),  # Blog list
    path("post/", views.add_post, name="add_post")  # Add a post
]






























#from django.urls import path
#from . import views
#from .views import register, user_login, logout, dashboard, blog_detail, home, create_blog, category_posts
#
#urlpatterns = [
#    path("", home, name="home"),
#    path("create/", create_blog, name="create_blog"),
#    path("", views.blog_index, name="blog_index"),
#    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
#    path("category/<category>/", views.blog_category, name="blog_category"),
#    path("category/<str:category_name>/", category_posts, name="category_posts"),
#    path("register/", views.register, name="register"),
#    path("login/", user_login, name="login"),
#    path("logout/", views.logout, name="logout"),
#    path("dashboard/", views.dashboard, name="dashboard"),
#    path("blogs/", views.blog_index, name="blog_index"),
#    path("post/", views.add_post, name="add_post")
#]
