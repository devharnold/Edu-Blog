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
