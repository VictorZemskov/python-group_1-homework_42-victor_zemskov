from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from webapp.models import User, Article, Comment, Ratting

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'