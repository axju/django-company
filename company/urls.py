from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('page/<str:name>/', views.page, name='page'),
]
