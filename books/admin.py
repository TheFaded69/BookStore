from django.contrib import admin
from .models import Book, BookType, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ('authors', 'book_type')
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name')
    search_fields = ('first_name', 'last_name', 'middle_name')


@admin.register(BookType)
class BookTypeAdmin(admin.ModelAdmin):
    list_display = ('book_type',)
    search_fields = ('book_type',)