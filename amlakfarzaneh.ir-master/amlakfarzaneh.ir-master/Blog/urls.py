from django.urls import path

from Blog.views import ArticlesListView, ArticleDetailView

urlpatterns = [
    path('blogs/', ArticlesListView.as_view(), name='article_page'),
    path('blog/<slug:slug>/', ArticleDetailView.as_view(), name='articles_detail'),
]
