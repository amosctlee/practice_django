from django.urls import path
# from .views import (
#     article_list_view,
#     article_detail_view,
# )
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    # my_fbv,
    CourseView,
)

# app_name = 'blog'
app_name = 'article'

urlpatterns = [
    # path('', ArticleListView.as_view(), name='article-list'),
    # path('<int:id>', ArticleDetailView.as_view(), name='article-detail'),
    # path('create/', ArticleCreateView.as_view(), name='article-create'),
    # path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    # path('', my_fbv, name='courses-list'),
    path('', CourseView.as_view(template_name='contact.html'), name='courses-list')
]
