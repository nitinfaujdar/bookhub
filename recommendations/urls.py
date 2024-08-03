from django.urls import path
from .views import BookRecommendationListCreateView, BookRecommendationDetailView, BookSearchView

urlpatterns = [
    path('recommendations/', BookRecommendationListCreateView.as_view(), name='recommendation-list-create'),
    path('recommendations/<int:pk>/', BookRecommendationDetailView.as_view(), name='recommendation-detail'),
    path('search/<str:query>/', BookSearchView.as_view(), name='book-search'),
]
