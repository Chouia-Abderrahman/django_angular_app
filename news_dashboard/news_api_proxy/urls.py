# news_api_proxy/urls.py

from django.urls import path
from .views import (fetch_news, get_news_by_country, get_news_by_category, get_all_news_in_database,
                    get_news_by_source, get_news_by_query, get_news_by_description)

urlpatterns = [
    path('fetch-news/', fetch_news, name='fetch_news'),
    path('get-news-by-category/<str:category>/', get_news_by_category, name='get_news_by_category'),
    path('get-news-by-country/<str:country>/', get_news_by_country, name='get_news_by_country'),
    path('get-news-by-source/<str:source>/', get_news_by_source, name='get_news_by_source'),
    path('get-news-by-query/<str:query>/', get_news_by_query, name='get_news_by_query'),
    path('get-news-by-description/<str:description>/', get_news_by_description, name='get_news_by_description'),
    path('get-all-news-in-database/', get_all_news_in_database, name='get_all_news_in_database'),
]
