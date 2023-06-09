from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from app.models import *


##this will be connecting to the 'comment view'
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ["content"]


##user creator??
class CustomUserCreatingForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SearchForm(forms.Form):
    query = forms.CharField(label="Search", max_length=50, required=True)


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["Title", "content", "category"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "last_name", "bio"]
