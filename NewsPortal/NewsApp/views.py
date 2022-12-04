from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
from django.http import HttpResponse


class PostsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


def pages(request):
    number = request.GET.get('number')

    try:
        result = int(number)
        html = f"<html><body>{result}</body></html>"
    except (ValueError, TypeError):
        html = f"<html><body>Invalid input.</body></html>"

    return HttpResponse(html)
