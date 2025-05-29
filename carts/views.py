from asyncore import write

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from books.models import Book
from .models import Cart, CartItem

def cart(request):
    user = request.user
    try:
        cart_detail = Cart.objects.get(user=user, deleted=False)
        cart_items = CartItem.objects.filter(cart=cart_detail, deleted=False).select_related('book')
    except Cart.DoesNotExist:
        cart_items = []

    total_price = sum(item.get_total_price() for item in cart_items)

    return render(request, 'carts/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def update_cart(request, book_id, delta):
    print(f"User: {request.user}")
    print(f"Book ID: {book_id}")
    print(f"Delta: {delta}")

    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Пользователь не авторизован'}, status=403)

    user = request.user
    book = Book.objects.get(id=book_id)

    cart, created = Cart.objects.get_or_create(user=user)
    if created:
        cart.save()

    cart_item, created = CartItem.objects.get_or_create(cart_id=cart.id, book_id=book.id)

    if not created:
        print(cart_item.quantity)
        cart_item.quantity += delta
        print(cart_item.quantity)
        if cart_item.quantity <= 0:
            cart_item.delete()
            return JsonResponse({
                'quantity': 0,
                'cart_count': cart.items.count(),
            })
        else:
            cart_item.save()
    else:
        cart_item.quantity = 1
        cart_item.save()


    return JsonResponse({
        'quantity': cart_item.quantity,
    })