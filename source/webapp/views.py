from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView
from webapp.models import User, Article, Comment, Ratting
from webapp.forms import ArticleSearchForm, ArticleForm
from django.urls import reverse_lazy

# Create your views here.

class ArticleListView(ListView, FormView):
    model = Article
    template_name = 'article_list.html'
    form_class = ArticleSearchForm

    def get_queryset(self):
        article_name = self.request.GET.get('article_name')
        if article_name:
            return self.model.objects.filter(title__icontains=article_name)
        else:
            return self.model.objects.all()

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_create.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_list')



