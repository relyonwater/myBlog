from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.


def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    '''str = ("title = %s, category = %s, date_time = %s, content = %s " %
           (post.title, post.category, post.date_time, post.content))'''
    return render(request, 'post.html', {'post': post})
