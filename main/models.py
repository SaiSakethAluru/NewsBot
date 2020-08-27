from django.db import models


# Create your models here.
class NewsArticles(models.Model):
    article_title = models.TextField()
    article_content = models.TextField()
    article_date = models.DateTimeField()
    article_source = models.TextField()
    article_url = models.URLField()

    def __str__(self):
        return self.article_title


