# blog/forms.py

from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Add a comment!"}
        )
    )

# For both author and body, use a CharField class to control how the form element should be rendered on the page
# The author field has the forms.
# The TextInput widget tells django to load the field as an HTML text input element in the templates
# The body field uses a forms.TextArea widget instead
