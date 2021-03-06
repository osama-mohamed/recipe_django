from django.urls import path

from .views import (
  article_create_view,
  article_update_view,
  article_delete_view,
  article_detail_view,
  all_articles_user_view,
)

app_name = 'articles'

urlpatterns = [
  path('my/', all_articles_user_view, name='all-user-articles'),
  path('create/', article_create_view, name='create'),
  path('<slug:slug>/update/', article_update_view, name='update'),
  path('<slug:slug>/delete/', article_delete_view, name='delete'),
  path('<slug:slug>/', article_detail_view, name='detail'),
]
