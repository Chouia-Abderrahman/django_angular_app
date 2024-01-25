from django.db import models


# Create your models here.
class NewsArticle(models.Model):

    source_id = models.CharField(max_length=255, null=True)
    source_name = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(unique=True)
    url_to_image = models.URLField(null=True, blank=True)
    published_at = models.DateTimeField(null=True)
    content = models.TextField(null=True, blank=True)
    # These im going to custom fill since they're not returned by default with
    # the articles
    category = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
