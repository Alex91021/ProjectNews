import django_filters
from django_filters import FilterSet, ModelChoiceFilter
from django_filters.widgets import RangeWidget

from .models import Post, PostCategory


class PostFilter(django_filters.FilterSet):
    #DateCreation = django_filters.CharFilter(lookup_expr='iexact', widget=RangeWidget(attrs={'placeholder': 'DD/MM/YYYY'}))

    class Meta:
        model = Post
        fields = {
            'postCategory': ['exact'],
            'title': ['icontains'],
            'rating': ['gte'],
            'categoryType': ['exact'],
            'dateCreation': ['exact'],
        }
