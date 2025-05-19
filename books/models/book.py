from django.db import models

from common.base_model import BaseModel

class Book(BaseModel):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author', blank=True)
    book_type = models.ManyToManyField('BookType', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
