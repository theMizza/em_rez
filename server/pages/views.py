from django.shortcuts import render
from django.http import Http404
from .models import StaticPages
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def static_page_handler(request, slug):
    try:
        page = StaticPages.objects.get(slug=slug)
    except Exception:
        raise Http404('Page not found')

    context = {'title': page.title}
    texts = page.page_texts.all()
    for text in texts:
        context[text.name] = text.value

    image_groups = page.images.all()
    for image_group in image_groups:
        context[image_group.value] = image_group.group_images.all()

    return render(request, page.template_path, context)
