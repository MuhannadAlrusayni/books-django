import html

from django.contrib import admin
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import django.core.validators

# Create your models here.

class Book(models.Model):
    BOOKS_GENRE = {
        "FIC": "Fiction",
        "NVL": "Novel",
        "HRR": "Horror"
    }
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    genre = models.CharField(max_length=3, choices=BOOKS_GENRE)
    rating = models.IntegerField(validators = [
        MaxValueValidator(5),
        MinValueValidator(1)
    ])
    
    @admin.display(ordering="rating", description="Rating")
    def rating_as_starts(self):
        match self.rating:
            case 1: return "⭐"
            case 2: return "⭐⭐"
            case 3: return "⭐⭐⭐"
            case 4: return "⭐⭐⭐⭐"
            case 5: return "⭐⭐⭐⭐⭐"
            case _: return ""

    def clean(self) -> None:
        self.title = html.escape(self.title)
        self.author = html.escape(self.author)
        return super().clean()


class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=50)
    comment = models.TextField(max_length=1500)
    date = models.DateField()
    
    def clean(self):
        self.reviewer_name = html.escape(self.reviewer_name)
        self.comment = html.escape(self.comment)
        return super().clean()