from django.core.mail import send_mail
from django.db.models import Count
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView

from Blog.models import Article
from Home.forms import AdvertisingForm
from Home.models import Header, Footer, AboutUs, Advertising
from property.models import Category


# Create your views here.


class HomeView(TemplateView):
    template_name = 'Home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # start header---------------
        context['header'] = Header.objects.filter(is_main=True).first()
        # end header-----------------

        # start footer----------------
        context['footer'] = Footer.objects.filter(is_main=True).first()
        # end footer------------------

        # start about-----------------
        context['about'] = AboutUs.objects.filter(is_main=True).first()
        # end about-----------------
        context['articles'] = Article.objects.all().order_by('-id')[:12]
        # start property---------------
        categories = list(
            Category.objects.annotate(products_count=Count('product_categories')).filter(
                products_count__gt=0).order_by(
                'id'))
        categories_products = []
        for category in categories:
            item = {
                'title': category.title,
                'image': category.image,
                'slug': category.slug,
                'url_slug': category.url_slug,
                'products': list(category.product_categories.all())
            }
            categories_products.append(item)
        context['options'] = categories_products
        # end property----------------------------

        return context


def add_phone_number(request):
    header = Header.objects.filter(is_main=True).first()
    footer = Footer.objects.filter(is_main=True).first()
    if request.method == 'POST':
        form = AdvertisingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            text = form.cleaned_data.get('text')
            new_advertising = Advertising(name=name, phone=phone, text=text)
            new_advertising.save()
            send_mail(
                'آگهی جدید',
                f'{name}\n{phone}\n{text}',
                'ali.naseri3179@gmail.com',
                ['realstatefarzaneh@gmail.com'],
                fail_silently=False,
            )
            return redirect(reverse('home_page'))
    else:
        form = AdvertisingForm()

    return render(request, 'Home/adv.html', {'form': form, 'header': header, 'footer': footer})
