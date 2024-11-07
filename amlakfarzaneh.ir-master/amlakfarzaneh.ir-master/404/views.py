from django.shortcuts import render

from Home.models import Footer


def error_404(request, exception):
    footer = Footer.objects.filter(is_main=True).first()
    return render(request, '404.html', status=404, context={'footer': footer})
