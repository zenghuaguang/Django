import base64

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from qb.models import Article, Image


def index(request):
    article_list = Article.objects.all()
    user = request.user if request.user.is_authenticated() else None
    paginator = Paginator(article_list, 10)
    page = request.GET.get('page')
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)

    content = {
        'user': user,
        'article_list': article_list,
    }
    return render(request, 'qb/index.html', content)


def image_index(request):
    article_list = Image.objects.all()[:250]
    print article_list[0]
    user = request.user if request.user.is_authenticated() else None
    paginator = Paginator(article_list, 5)
    page = request.GET.get('page')
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)

    content = {
        'user': user,
        'article_list': article_list,
    }
    return render(request, 'qb/image_index.html', content)


def test(request):
    article = Article.objects.all()[1]
    print article
    img_data=article.user_image
    img_data=base64.b64encode(img_data)
    img_data=img_data.decode()
    img_tag = '<img alt="sample" src="data:image/png;base64,{0}">'.format(img_data)
    return HttpResponse(img_tag)