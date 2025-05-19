from django.db import models

from common.base_model import BaseModel

class CartItem(BaseModel):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()