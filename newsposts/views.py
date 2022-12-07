# Create your views here.
from django.shortcuts import render
from .models import Article, Tags
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import django.http as http

# Create your views here.
def index(request):
    articles_list = Article.objects.all()
    return render(request, 'newsposts/list.html', {'articles_list': articles_list})


def detail(reques, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена(")

    b = a.tags.all()

    return render(reques, 'newsposts/detail.html', {'article': a, 'article_tags': b})

def all_article_tags(request, slug):
    s = Tags.objects.get(slug__iexact=slug)
    a = Article.objects.all()
    return render(request, 'newsposts/tags.html', {'tags': s, 'article': a})


