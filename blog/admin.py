# we need to register our models to the django admin site,
# otherwise the admin won't see what we created


from django.contrib import admin
from blog.models import Category, Comment, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
