from django.urls import path
from django.views.generic.detail import DetailView

from . import views
from company.views import IndexView, PageDetailView, PostDetailView, PostListView, PostArticleListView, PostNewsListView

app_name = 'company'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('page/<str:name>/', PageDetailView.as_view(), name='page'),
    path('post/', PostListView.as_view(), name='post-list'),
    path('article/', PostArticleListView.as_view(), name='article-list'),
    path('news/', PostNewsListView.as_view(), name='news-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
