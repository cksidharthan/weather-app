from django.db import models
from datetime import datetime


# Create your models here.
class SearchData(models.Model):
    search_location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=datetime.now)
