from django.db import models

from common.base_model import BaseModel

class Cart(BaseModel):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
