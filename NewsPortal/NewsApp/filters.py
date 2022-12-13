from django_filters import FilterSet, ModelChoiceFilter
from .models import Post, PostCategory


class PostFilter(FilterSet):
    # Category = ModelChoiceFilter(
    #
    # )

    class Meta:
        model = Post
        fields = {
            'postCategory': ['exact'],
            'title': ['icontains'],
            'rating': ['gte'],
            'categoryType': ['icontains'],
        }
