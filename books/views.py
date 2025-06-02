from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest

from books.models import Book, Author, BookType
from carts.models import Cart, CartItem

class BookStoreView(ListView):
    model = Book
    template_name = 'books/book_store.html'
    context_object_name = 'books'
    paginate_by = None

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('authors', 'book_type')

        name_query = self.request.GET.get('name')
        author_id = self.request.GET.get('author')
        type_id = self.request.GET.get('type')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if name_query:
            queryset = queryset.filter(name__icontains=name_query)
        if author_id:
            queryset = queryset.filter(authors__id=author_id)
        if type_id:
            queryset = queryset.filter(book_type__id=type_id)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['authors'] = Author.objects.all()
        context['book_types'] = BookType.objects.all()

        context['name_query'] = self.request.GET.get('name', '')
        context['author_id'] = self.request.GET.get('author', '')
        context['type_id'] = self.request.GET.get('type', '')
        context['min_price'] = self.request.GET.get('min_price', '')
        context['max_price'] = self.request.GET.get('max_price', '')

        cart_data = {}
        if self.request.user.is_authenticated:
            try:
                cart = self.request.user.carts.get()
                cart_items = cart.items.select_related('book').all()
                cart_data = {item.book.id: item.quantity for item in cart_items}
            except Cart.DoesNotExist:
                pass #todo

        context['cart_data'] = cart_data

        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book.html'
    context_object_name = 'book'
    slug_field = 'id'
    slug_url_kwarg = 'book_id'

    def get_object(self, queryset=None):
        return get_object_or_404(Book, id=self.kwargs['book_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cart_item'] = None

        if self.request.user.is_authenticated:
            try:
                cart = self.request.user.carts.get()
                context['cart_item'] = cart.items.get(book=self.object)
            except CartItem.DoesNotExist:
                pass #todo

        return context

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponseBadRequest("Неподдерживаемый метод запроса")