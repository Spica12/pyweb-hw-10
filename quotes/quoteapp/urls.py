from django.urls import path
from . import views
from . import seed

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('tag/', views.tag, name='tag'),
    path('quote/', views.quote, name='quote'),
    path('author/', views.author, name='author'),
    path('detail/<author_fullanme>', views.detail, name='detail'),
    path('delete_all_quotes/', views.delete_all_quotes, name='delete_all_quotes'),
    path('delete_all_authors/', views.delete_all_authors, name='delete_all_authors'),
    path('delete_all_tags/', views.delete_all_tags, name='delete_all_tags'),
    path('seed_authors/', seed.seed_authors, name='seed_authors'),
    path('seed_quotes/', seed.seed_quotes, name='seed_quotes'),
]
