from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('city/<slug:city>/', views.article_list_city, name='article-list-city'),
    path('create/', views.ArticleCreateView.as_view(), name='article-create'),
    path('detail/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('update/<int:pk>/', views.ArticleUpdateView.as_view(), name='article-update'),
    path('delete/<int:pk>/', views.ArticleDeleteView.as_view(), name='article-delete'),
]
