from django.views.generic import ListView, DetailView
from .models import Author, Category, Post, PostCategory


class AuthorsList(ListView):
    model = Author
    ordering = 'authorUser'
    template_name = 'authors.html'
    context_object_name = 'authors'


class CategoriesList(ListView):
    model = Category
    ordering = 'name'
    template_name = 'categories.html'
    context_object_name = 'categories'


class PostsList(ListView):
    model = Post
    ordering = 'name'
    template_name = 'flatpages/posts.html'
    context_object_name = 'posts'


class PostCategoriesList(ListView):
    model = PostCategory
    ordering = 'name'
    template_name = 'post-categories.html'
    context_object_name = 'post-categories'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'author.html'
    context_object_name = 'author'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCategoryDetail(DetailView):
    model = PostCategory
    template_name = 'post-category.html'
    context_object_name = 'post-category'
