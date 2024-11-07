from django.views.generic import ListView, DetailView

from Home.models import Footer, Header
from .models import Article, Article_Detail


# Create your views here.

class ArticlesListView(ListView):
    model = Article
    paginate_by = 9
    template_name = 'Blog/blog.html'
    context_object_name = 'articles'
    ordering = ('-id',)

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(*args, **kwargs)
        context['header'] = Header.objects.filter(is_main=True).first()
        # end header-----------------

        # start footer----------------
        context['footer'] = Footer.objects.filter(is_main=True).first()
        # end footer------------------
        return context

    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        query = query.filter(is_active=True)
        return query


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'Blog/blogPost.html'
    context_object_name = 'article'

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        context['header'] = Header.objects.filter(is_main=True).first()
        # end header-----------------
        # start footer----------------
        context['footer'] = Footer.objects.filter(is_main=True).first()
        # end footer------------------

        return context
