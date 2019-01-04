from django.urls import path
from django.views.generic.detail import DetailView

from . import views
from company.views import IndexView, FeatureDetailView, FeatureListView, ProductDetailView

app_name = 'company'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('feature/', FeatureListView.as_view(), name='feature-list'),
    path('feature/<int:pk>/', FeatureDetailView.as_view(), name='feature-detail'),

    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
