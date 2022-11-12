from django.shortcuts import render
from .models import Article, Comment, Party, City
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import django.http as http

# Create your views here.
def index(request):
    # latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    latest_articles_list = Article.objects.all()
    return render(request, 'main/list.html', {'latest_articles_list': latest_articles_list})


def detail(reques, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдна(")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    b = a.party.all()[0]
    c = a.city.all()[0]

    return render(reques, 'main/detail.html', {'article': a, 'article_party': b, 'article_city': c, 'latest_comments_list': latest_comments_list})

def all_article_party(request, slug):
    s = Party.objects.get(slug__iexact=slug)
    a = Article.objects.all()
    return render(request, 'main/party.html', {'party': s, 'article': a})

def all_article_city(request, slug):
    s = City.objects.get(slug__iexact=slug)
    a = Article.objects.all()
    return render(request, 'main/city.html', {'city': s, 'article': a})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена(")  
    a.comment_set.create(name_user = request.user, comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('main:detail', args = (a.id,)))


def delete_comment(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена(")  
    a.comment_set.delete()

    return HttpResponseRedirect(reverse('main:detail', args = (a.id,)))