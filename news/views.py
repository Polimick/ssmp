from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
# Create your views here.

def index(request):
    try:
        a = Article.objects.all()
    except:
        raise Http404("Статья не найдена(")
    
    reverse_list = a.order_by('-id')[:10]

    return render(request, 'news/list.html', {'article': reverse_list})






