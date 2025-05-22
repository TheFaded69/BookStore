from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render

from books.models import Book
from users.forms import RegisterForm


def book_store(request):
    return render(request, 'books/book_store.html')

def book(request: WSGIRequest) -> HttpResponse :
    try:
        if request.method == "GET":
            book_id = request.GET.get('book_id')
            book = Book.objects.get(id=book_id)
            return render(request, 'books/book.html', {'book': book})
        else:
            return HttpResponseBadRequest()
    except:
        return HttpResponseBadRequest()

