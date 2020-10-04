from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


class ArticleListView(ListView):
    model=Article
    template_name="articles/article_list.html"
    context_object_name='articles'
    ordering = ['-date_posted']
    def to_python(self, value):
        print(self.slug,"\n\n\n")

class ArticleDetailView(DetailView):
    model=Article
    template_name="articles/article_detail.html"
    context_object_name="article"



def article_list_city(request,city):
    context = {
        'articles': Article.objects.filter(city=city.upper())
    }
    return render(request, 'articles/article_list.html', context)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model=Article
    template_name="articles/article_form.html"
    fields = ['title','content','date_of_action','city']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView ):
    model=Article
    template_name="articles/article_form.html"
    fields = ['title','content','date_of_action','city']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = '/articles'

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False
