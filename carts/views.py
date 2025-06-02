from django.shortcuts import render, get_object_or_404 , redirect
from django.views import View

from books.models import Book
from .models import Cart, CartItem

#todo func to CBV
def carts(request):
    try:
        user = request.user

        cart_detail = Cart.objects.get(user=user, deleted=False)
        cart_items = CartItem.objects.filter(cart=cart_detail, deleted=False).select_related('book')
    except Cart.DoesNotExist:
        cart_items = []

    return render(request, 'carts/cart.html', {
        'cart_items': cart_items
    })

class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        book_id = request.POST.get('book_id')
        if not book_id:
            return redirect('book_store')

        book = get_object_or_404(Book, id=book_id)

        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)

        if created:
            cart_item.save()
        cart_item.quantity += 1
        cart_item.save()

        return redirect(request.META.get('HTTP_REFERER', 'book_store'))


class RemoveFromCartView(View):
    def post(self, request, *args, **kwargs):
        book_id = request.POST.get('book_id')
        if not book_id:
            return redirect('book_store')

        book = get_object_or_404(Book, id=book_id)

        try:
            cart = request.user.carts.get()
            cart_item = cart.items.get(book=book)
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
        except (Cart.DoesNotExist, CartItem.DoesNotExist):
            pass

        return redirect(request.META.get('HTTP_REFERER', 'book_store'))