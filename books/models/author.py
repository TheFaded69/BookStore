from django.db import models

from common.base_model import BaseModel

class Author(BaseModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
