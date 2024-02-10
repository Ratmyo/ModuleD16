from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import ArticleForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


class ArticlesList(ListView):
    model = Article
    ordering = 'title'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 10


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('board.add_article',)
    form_class = ArticleForm
    model = Article
    template_name = 'article_edit.html'


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('board.change_article',)
    form_class = ArticleForm
    model = Article
    template_name = 'article_edit.html'


class ResponseList(PermissionRequiredMixin, ListView):
    model = UserResponse
    ordering = 'article'
    template_name = 'responses.html'
    context_object_name = 'responses'
    paginate_by = 10

    def get_queryset(self):
        queryset = UserResponse.objects.filter(article__author=self.request.user) #проверить
        return queryset
