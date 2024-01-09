from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your tests here.

from .models import Book, BookReview

class BookModelTest(TestCase):
    def test_ensure_rating_between_1_and_5(self):
        """
        ensure rating between 1 and 5
        """
        today = timezone.now().date()
        book1 = Book(title="title", author="author", published_date=today, genre="FIC", rating=1)
        book1.full_clean()
        book2 = Book(title="title", author="author", published_date=today, genre="FIC", rating=5)
        book2.full_clean()
        book3 = Book(title="title", author="author", published_date=today, genre="FIC", rating=6)
        with self.assertRaises(ValidationError):
            book3.full_clean()
    
    def test_ensure_all_values_sanitized(self):
        """
        ensure model values sanitized 
        """
        today = timezone.now().date()
        book = Book(title="title\"title<script>", author="author\"<script>alert(\"hi from js\")</script>", published_date=today, genre="FIC", rating=1)
        book.full_clean()
        book.save()
        self.assertNotEqual(book.title, "title\"title<script>")
        self.assertNotEqual(book.author, "author\"<script>alert(\"hi from js\")</script>")

        review = BookReview(book=book, reviewer_name="name\"<script>use js</script>", comment="blah blah..\"<script>use js</script>", date=today)
        review.full_clean()
        self.assertNotEqual(review.reviewer_name, "name\"<script>use js</script>")
        self.assertNotEqual(review.comment, "blah blah..\"<script>use js</script>")

    def test_rating_as_stars(self):
        """
        ensure rating as starts works for 1 to 5
        """
        today = timezone.now().date()
        book1 = Book(title="title", author="author", published_date=today, genre="FIC", rating=1)
        self.assertEqual(book1.rating_as_starts(), "⭐")
        book2 = Book(title="title", author="author", published_date=today, genre="FIC", rating=2)
        self.assertEqual(book2.rating_as_starts(), "⭐⭐")
        book3 = Book(title="title", author="author", published_date=today, genre="FIC", rating=3)
        self.assertEqual(book3.rating_as_starts(), "⭐⭐⭐")
        book4 = Book(title="title", author="author", published_date=today, genre="FIC", rating=4)
        self.assertEqual(book4.rating_as_starts(), "⭐⭐⭐⭐")
        book5 = Book(title="title", author="author", published_date=today, genre="FIC", rating=5)
        self.assertEqual(book5.rating_as_starts(), "⭐⭐⭐⭐⭐")