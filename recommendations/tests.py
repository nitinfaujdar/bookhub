from django.test import TestCase
from .models import BookRecommendation
from django.contrib.auth.models import User

class BookRecommendationTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser', password='testpassword')
        BookRecommendation.objects.create(
            title="Test Book",
            author="Test Author",
            description="Test Description",
            cover_image="http://example.com/image.jpg",
            rating=4.5,
            genre="Fiction",
            publication_date="2021-01-01",
            user=user
        )

    def test_book_recommendation_creation(self):
        book = BookRecommendation.objects.get(title="Test Book")
        self.assertEqual(book.author, "Test Author")
