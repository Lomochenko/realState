from django.contrib.admin.templatetags.admin_list import pagination
from django.views.generic import ListView

from Home.models import Header, Footer
from property.models import Estate


# Create your views here.

class EstateListView(ListView):
    model = Estate
    template_name = 'property/property-list.html'
    context_object_name = 'estates'
    ordering = ('id',)
    paginate_by = 12

    def get_context_data(self, *args, **kwargs):
        context = super(EstateListView, self).get_context_data(*args, **kwargs)
        # start header---------------
        context['header'] = Header.objects.filter(is_main=True).first()
        # end header-----------------

        # start footer----------------
        context['footer'] = Footer.objects.filter(is_main=True).first()
        # end footer------------------
        return context

    def get_queryset(self):
        query = super(EstateListView, self).get_queryset()
        query = query.all()
        category_name = self.kwargs.get('url_slug')
        if category_name is not None:
            query = query.filter(category__url_slug=category_name)
        return query
