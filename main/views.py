from dateutil import parser
from django.shortcuts import render
from newsapi import NewsApiClient

from main.models import NewsArticles


def homepage(request):
    api = NewsApiClient('fc8e2ae2cdaf489c9bc80e52c8d7d2f4')
    articles = api.get_top_headlines()
    news_articles = []
    if articles['status'] == 'ok':
        for i in range(10):
            article = articles['articles'][i]
            article_obj = NewsArticles(article_title=article['title'],
                                       article_content=article['content'],
                                       article_date=parser.parse(article['publishedAt']),
                                       article_url=article['url'],
                                       article_source=article['source']['name'])
            news_articles.append(article_obj)

    return render(request=request,
                  template_name='main/home.html',
                  context={'news_articles': news_articles})
