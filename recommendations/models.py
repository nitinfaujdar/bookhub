from django.db import models
from django.contrib.auth.models import User

class BookRecommendation(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.URLField()
    rating = models.FloatField(default=0.0)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
