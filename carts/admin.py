# carts/admin.py
from django.contrib import admin
from .models import Cart, CartItem
from books.models import Book

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    fields = ('book', 'quantity', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fk = True
    show_change_link = True

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "book":
            kwargs["queryset"] = Book.objects.all().order_by('name')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    search_fields = ('user__username',)
    inlines = [CartItemInline]
    readonly_fields = ('created_at', 'updated_at')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'book', 'quantity', 'created_at', 'updated_at')
    list_filter = ('cart', 'book')
    search_fields = ('book__name', 'cart__user__username')
    readonly_fields = ('created_at', 'updated_at')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "book":
            kwargs["queryset"] = Book.objects.all().order_by('name')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)