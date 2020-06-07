from django.urls import path

from .views import (
    ArticleListView ,
    ArticleUpdateView , 
    ArticleDetailView , 
    ArtcleDeleteView,
    ArticleCreateView
)


urlpatterns = [
    #path('',ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view() , name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view() , name='article_detail'),
    path('<int:pk>/delete/', ArtcleDeleteView.as_view() , name='article_delete'),
    path('' , ArticleListView.as_view() , name='article_list'),
    path('new/', ArticleCreateView.as_view() , name='article_new'),
]