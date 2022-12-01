from django.urls import path
from .views import PostsList, PostDetail

urlpatterns = [path('posts/', PostsList.as_view()),
               path('posts/<int:pk>', PostDetail.as_view())
]
