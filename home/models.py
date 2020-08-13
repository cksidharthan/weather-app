from django.db import models


class HomeSearch(models.Model):
    search_location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
