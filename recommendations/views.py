import requests
from rest_framework import generics, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import BookRecommendation
from .serializers import BookRecommendationSerializer

class BookRecommendationListCreateView(generics.ListCreateAPIView):
    queryset = BookRecommendation.objects.all()
    serializer_class = BookRecommendationSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['genre', 'rating', 'publication_date']
    ordering_fields = ['rating', 'publication_date']
    search_fields = ['title', 'author', 'description']

class BookRecommendationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookRecommendation.objects.all()
    serializer_class = BookRecommendationSerializer

class BookSearchView(generics.GenericAPIView):
    serializer_class = BookRecommendationSerializer

    def get(self, request, query):
        url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
        response = requests.get(url)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({"error": "Unable to fetch data"}, status=status.HTTP_400_BAD_REQUEST)
