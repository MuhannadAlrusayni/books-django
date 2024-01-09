import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Book, BookReview

# Register your models here.


class BookReviewInline(admin.StackedInline):
    model = BookReview
    extra = 1
    list_display = ["book", "reviewer_name", "comment", "date"]
    ordering = ["date"]


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_date", "genre", "rating_as_starts"]
    search_fields = ["title", "author"]
    list_filter = ["genre", "published_date"]
    inlines = [BookReviewInline]
    actions = ["export_books_as_csv"]
    ordering = ["published_date", "title", "author"]

    @admin.action(description="Export selected books in CSV format")
    def export_books_as_csv(self, request, queryset):
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="books.csv"'},
        )

        writer = csv.writer(response)
        writer.writerow(["title", "author", "published_date", "genre", "rating"])
        for obj in queryset:
            writer.writerow([obj.title, obj.author, obj.published_date, obj.genre, obj.rating])

        return response


admin.site.register(Book, BookAdmin)