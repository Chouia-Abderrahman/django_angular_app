from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import NewsArticle
from newsapi import NewsApiClient
from .serializers import NewsArticleSerializer

api_key = 'you_api_key'

@api_view(['GET'])
def fetch_news(request):

    newsapi = NewsApiClient(api_key=api_key)

    top_headlines = newsapi.get_top_headlines()

    for article_data in top_headlines['articles']:
        create_if_not_in_database(article_data)

    return Response({'message': 'News fetched successfully'})

def add_additional_info(article, additional_info):
    for info in additional_info.keys():
        if info == "category":
            article.category = additional_info[info]
        elif info == "language":
            article.language = additional_info[info]
        elif info == "country":
            article.country = additional_info[info]
    article.save()

def create_if_not_in_database(article_data, **additional_info):
    url = article_data['url']

    # Get an existing article or create a new one if it doesn't exist
    news_article, created = NewsArticle.objects.get_or_create(
        url=url,
        defaults={
            'source_id': article_data['source']['id'],
            'source_name': article_data['source']['name'],
            'author': article_data['author'],
            'title': article_data['title'],
            'description': article_data['description'],
            'url_to_image': article_data['urlToImage'],
            'published_at': article_data['publishedAt'],
            'content': article_data['content'],
        }
    )

    # If the article already exists, update its fields
    if not created:
        existing_article = NewsArticle.objects.get(url=url)
        # Update the fields
        existing_article.source_id = article_data['source']['id']
        existing_article.source_name = article_data['source']['name']
        existing_article.author = article_data['author']
        existing_article.title = article_data['title']
        existing_article.description = article_data['description']
        existing_article.url_to_image = article_data['urlToImage']
        existing_article.published_at = article_data['publishedAt']
        existing_article.content = article_data['content']
        existing_article.save()
        if additional_info:
            add_additional_info(existing_article, additional_info)
    else:
        if additional_info:
            add_additional_info(news_article, additional_info)


@api_view(['GET'])
def get_news_by_category(request, category):

    newsapi = NewsApiClient(api_key=api_key)
    news = newsapi.get_top_headlines(
        category=category
    )
    for new in news["articles"]:
        create_if_not_in_database(new, category=category)
    result_news = NewsArticle.objects.filter(category=category)
    serializer = NewsArticleSerializer(result_news, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_news_by_country(request, country):
    newsapi = NewsApiClient(api_key=api_key)
    news = newsapi.get_top_headlines(
        country=country
    )
    for new in news["articles"]:
        create_if_not_in_database(new, country=country)
    result_news = NewsArticle.objects.filter(country=country)
    serializer = NewsArticleSerializer(result_news, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_news_by_source(request, source):
    result_news = NewsArticle.objects.filter(source_name=source)
    serializer = NewsArticleSerializer(result_news, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_news_by_query(request,query):
    # query = request.GET.get('query', '')
    news = NewsArticle.objects.filter(title__icontains=query)
    serializer = NewsArticleSerializer(news, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_news_by_description(request, description):
    # description = request.GET.get('description', '')
    news = NewsArticle.objects.filter(description__icontains=description)
    serializer = NewsArticleSerializer(news, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_news_in_database(request):
    news = NewsArticle.objects.filter()
    serializer = NewsArticleSerializer(news, many=True)
    return Response(serializer.data)
