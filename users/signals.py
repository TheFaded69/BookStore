from django.contrib.auth import user_logged_in
from django.dispatch import receiver
from carts.models import Cart

@receiver(user_logged_in)
def create_cart_for_user(sender, request, user, **kwargs):
    print("user logged in")
    carts = Cart.objects.get_or_create(user=user)
    print(carts)
