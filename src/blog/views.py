
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import ArticleModelForm
from .models import Article
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)

from django.views import View

# BASE VIEW Class = VIEW


class CourseView(View):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    # def get(request, *args, **kwargs):
    #     return render(request, 'about.html', {})

# HTTP METHODS


def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request, 'about.html', {})


class ArticleCreateView(CreateView):

    template_name = 'article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'


class ArticleUpdateView(UpdateView):
    template_name = 'article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    # success_url = "/blog/"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('article:article-list')


class ArticleListView(ListView):
    template_name = 'article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


# def article_list_view(request):
#     query_set = Article.objects.all()
#     context = {
#         'query_set': query_set
#     }
#     return render(request, 'article_list.html', context=context)


# def article_detail_view(request, id):
#     obj = get_object_or_404(Article, id=id)
#     context = {
#         'object': obj
#     }
#     return render(request, 'article_detail.html', context=context)
