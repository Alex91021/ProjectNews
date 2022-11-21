from django.urls import path
from .views import * #AuthorsList, CategoriesList, PostsList, PostCategoriesList, \
                  #AuthorDetail, CategoryDetail, PostDetail, PostCategoryDetail

urlpatterns = [path('', AuthorsList.as_view()),
               path('', CategoriesList.as_view()),
               path('', PostsList.as_view()),
               path('', PostCategoriesList.as_view()),
               path('<int:pk>', AuthorDetail.as_view()),
               path('<int:pk>', CategoryDetail.as_view()),
               path('<int:pk>', PostDetail.as_view()),
               path('<int:pk>', PostCategoryDetail.as_view()),
               ]
