from dateutil import parser
from django.shortcuts import render
from newsapi import NewsApiClient

from main.NewsArticles import NewsArticles
from main.forms import NewsFilterForm

news_articles = []
form = None


def get_top_articles(country=None, category=None):
    api = NewsApiClient('fc8e2ae2cdaf489c9bc80e52c8d7d2f4')
    if country == '':
        country = None
    if category == '':
        category = None
    articles = api.get_top_headlines(category=category, country=country)
    global news_articles
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


def homepage(request):
    global news_articles
    global form
    if request.method == 'POST':
        form = NewsFilterForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data['country_dropdown']
            category = form.cleaned_data['category_dropdown']
            get_top_articles(country=country, category=category)
    else:
        form = NewsFilterForm()
        get_top_articles()
    return render(request=request,
                  template_name='main/home.html',
                  context={'news_articles': news_articles, 'form': form})


def read_page(request):
    global news_articles
    global form
    if not form:
        form = NewsFilterForm()
    return render(request=request,
                  template_name='main/read.html',
                  context={'news_articles': news_articles, 'form': form})
