from django_filters import FilterSet
from .models import Post, Author


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            # 'author': ['icontains'],
            'title': ['icontains'],
            'rating': ['gte'],
        }
