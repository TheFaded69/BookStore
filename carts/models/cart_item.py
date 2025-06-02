from django.db import models

from common.base_model import BaseModel

class CartItem(BaseModel):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False, default=0)

    def get_total_price(self):
        return self.book.price * self.quantity