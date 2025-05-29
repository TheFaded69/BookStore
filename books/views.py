from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book, Author, BookType

from books.models import Book
from users.forms import RegisterForm


def book_store(request):
    author_id = request.GET.get('author')
    type_id = request.GET.get('type')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    books = Book.objects.all()

    if author_id:
        books = books.filter(authors__id=author_id)
    if type_id:
        books = books.filter(book_type__id=type_id)
    if min_price:
        books = books.filter(price__gte=min_price)  # price >= min_price
    if max_price:
        books = books.filter(price__lte=max_price)  # price <= max_price

    books = books.distinct().prefetch_related('authors', 'book_type')

    authors = Author.objects.all()
    book_types = BookType.objects.all()

    return render(request, 'books/book_store.html', {
        'books': books,
        'authors': authors,
        'book_types': book_types,
    })

def book(request: WSGIRequest, book_id) -> HttpResponse :
    try:
        if request.method == "GET":
            book_detail = get_object_or_404(Book, id=book_id)
            return render(request, 'books/book.html', {'book': book_detail})
        else:
            return HttpResponseBadRequest()
    except:
        return HttpResponseBadRequest()

