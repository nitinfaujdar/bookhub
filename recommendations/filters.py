import django_filters
from .models import BookRecommendation

class BookRecommendationFilter(django_filters.FilterSet):
    class Meta:
        model = BookRecommendation
        fields = ['genre', 'rating', 'publication_date']
