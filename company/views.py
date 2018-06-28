from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views import View

from company.models import Portfolio, PORTFOLIO_CATEGORY, Post


class IndexView(View):
    def get(self, request):
        content = {}
        for category in PORTFOLIO_CATEGORY:
            content[category[0]+'s'] = Portfolio.objects.filter(category=category[0])
        return render(request, 'company/index.html', content)


class PageDetailView(TemplateView):
    template_name = 'company/default.html'

    def dispatch(self, request, *args, **kwargs):
        name = kwargs.get('name', 'default')
        self.template_name = 'company/pages/{}.html'.format(name)
        return super(PageDetailView, self).dispatch(request, *args, **kwargs)


class PostDetailView(DetailView):
    model = Post

class PostListView(ListView):
    model = Post
    paginate_by = 100

class PostArticleListView(PostListView):
    template_name = 'company/article_list.html'
    def get_queryset(self):
        return self.model.objects.filter(category='article')

class PostNewsListView(PostListView):
    template_name = 'company/news_list.html'
    def get_queryset(self):
        return self.model.objects.filter(category='news')
