from django.urls import path
from .views import AuthorsList, CategoriesList, PostsList, PostCategoriesList, \
                  AuthorDetail, CategoryDetail, PostDetail, PostCategoryDetail

urlpatterns = [path('authors/', AuthorsList.as_view()),
               path('category/', CategoriesList.as_view()),
               path('post/', PostsList.as_view()),
               path('postcategory/', PostCategoriesList.as_view()),
               path('<int:pk>', AuthorDetail.as_view()),
               path('<int:pk>', CategoryDetail.as_view()),
               path('<int:pk>', PostDetail.as_view()),
               path('<int:pk>', PostCategoryDetail.as_view()),
               ]
