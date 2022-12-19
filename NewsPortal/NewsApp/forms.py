from django import forms
from .models import Post


class ProductForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'categoryType',
            'dateCreation',
            'postCategory',
            'title',
        ]
