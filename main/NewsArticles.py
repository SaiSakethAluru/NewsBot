class NewsArticles():
    def __init__(self, article_title, article_content, article_date, article_url, article_source):
        self.article_title = article_title
        self.article_content = article_content
        self.article_date = article_date
        self.article_url = article_url
        self.article_source = article_source

    def __str__(self):
        return self.article_title
