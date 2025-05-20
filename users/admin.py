from django.contrib import admin
from users.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'password')
    search_fields = ('first_name', 'last_name', 'username', 'password')