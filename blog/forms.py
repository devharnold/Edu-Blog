# blog/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']  # Only the 'body' field should be included
        widgets = {
            "body": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Write your comment here..."})
        }

#class CommentForm(forms.ModelForm):
#    # This is a comment form
#    author = forms.CharField(
#        max_length=60,
#        widget=forms.TextInput(
#            attrs={"class": "form-control", "placeholder": "Your Name"}
#        ),
#    )
#    body = forms.CharField(
#        widget=forms.Textarea(
#            attrs={"class": "form-control", "placeholder": "Add a comment!"}
#        )
#    )

class PostForm(forms.ModelForm):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Name"})
    )
    
    body = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Add a text"})
    )

    class Meta:
        model = Post
        fields = ["title", "author", "body", "categories"]


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your blog here...'}),
            'categories': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_categories(self):
        categories = self.cleaned_data.get('categories')
        # Ensure that the categories are valid Category instances
        if categories:
            return categories
        return []


#class BlogForm(forms.ModelForm):
#    categories = forms.CharField(
#        max_length=200,
#        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter categories separated by commas"}),
#        required=False
#    )
#    
#    class Meta:
#        model = Post
#        fields = ["title", "body", "categories"]
#        widgets = {
#            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Blog Title"}),
#            "body": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Write your blog here..."}),
#            "categories": forms.CheckboxSelectMultiple(attrs={"class": "form-control"})
#        }

#class BlogForm(forms.ModelForm):
#    class Meta:
#        model = Post
#        fields = ["title", "body", "categories"]
#        widgets = {
#            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Blog Title"}),
#            "body": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Write your blog here..."}),
#            "categories": forms.CheckboxSelectMultiple()
#        }