from django.contrib import admin
from .models import Category, Product, Cart, Order, OrderItem
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "slug")

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "category",
        "price",
        "stock",
        "is_available",
    )

    list_filter = (
        "category",
        "is_available",
    )

    search_fields = (
        "name",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "product",
        "quantity",
        "added_at",
    )

admin.site.register(Order)
admin.site.register(OrderItem)