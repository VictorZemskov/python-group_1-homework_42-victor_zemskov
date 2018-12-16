from django.shortcuts import render
from django.views.generic import ListView, DetailView
from webapp.models import User, Article, Comment, Ratting

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'