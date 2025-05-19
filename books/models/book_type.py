from django.db import models

from common.base_model import BaseModel

class BookType(BaseModel):
    book_type = models.CharField(max_length=120)