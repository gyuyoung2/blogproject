from django.db.models import fields
from post.models import Page
from django import forms
from .models import Page
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'body']